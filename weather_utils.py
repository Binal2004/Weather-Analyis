"""
weather_utils.py
Reusable utility functions for Global Weather Data Analysis
Author: Binal Doshi | MSc AI & Data Science, University of Mumbai
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# ─── DATA LOADING ─────────────────────────────────────────────────────────────

def load_weather_data(filepath: str) -> pd.DataFrame:
    """Load and enrich weather CSV with derived time features."""
    df = pd.read_csv(filepath, parse_dates=['date'])
    df['year']       = df['date'].dt.year
    df['month']      = df['date'].dt.month
    df['month_name'] = df['date'].dt.strftime('%b')
    df['season']     = df['month'].map({
        12:'Winter', 1:'Winter',  2:'Winter',
         3:'Spring', 4:'Spring',  5:'Spring',
         6:'Summer', 7:'Summer',  8:'Summer',
         9:'Autumn',10:'Autumn', 11:'Autumn'
    })
    return df


# ─── DATA QUALITY ─────────────────────────────────────────────────────────────

def run_quality_checks(df: pd.DataFrame) -> pd.DataFrame:
    """Remove physically impossible weather values."""
    before = len(df)
    df = df[df['temp_max_c'] >= df['temp_min_c']]
    df = df[df['precipitation_mm'] >= 0]
    df = df[df['humidity_pct'].between(0, 100)]
    df = df[df['wind_speed_kmh'] >= 0]
    print(f"Quality check: {before:,} → {len(df):,} rows ({before - len(df)} removed)")
    return df


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame summarising missing values."""
    report = pd.DataFrame({
        'Missing': df.isnull().sum(),
        'Pct_Missing': (df.isnull().sum() / len(df) * 100).round(2)
    })
    return report[report['Missing'] > 0]


# ─── AGGREGATION HELPERS ──────────────────────────────────────────────────────

def city_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return per-city descriptive statistics."""
    return df.groupby('city').agg(
        Records      = ('date',            'count'),
        Avg_Temp_C   = ('temp_avg_c',      'mean'),
        Max_Temp_C   = ('temp_max_c',      'max'),
        Min_Temp_C   = ('temp_min_c',      'min'),
        Annual_Rain  = ('precipitation_mm','sum'),
        Avg_Humidity = ('humidity_pct',    'mean'),
        Avg_Wind_kmh = ('wind_speed_kmh',  'mean'),
    ).round(2)


def seasonal_rainfall(df: pd.DataFrame, city: str) -> pd.Series:
    """Average seasonal rainfall for a given city (mm/year)."""
    season_order = ['Spring', 'Summer', 'Autumn', 'Winter']
    years = df['year'].nunique()
    return (
        df[df['city'] == city]
        .groupby('season')['precipitation_mm']
        .sum()
        .reindex(season_order) / years
    )


# ─── STATISTICS ───────────────────────────────────────────────────────────────

def pearson_correlation(df: pd.DataFrame, col_a: str, col_b: str) -> dict:
    """Compute Pearson r between two columns."""
    r, p = stats.pearsonr(df[col_a].dropna(), df[col_b].dropna())
    return {'r': round(r, 4), 'p_value': round(p, 6),
            'significant': p < 0.05}


def anova_test(df: pd.DataFrame, group_col: str, value_col: str) -> dict:
    """One-way ANOVA across groups."""
    groups = [grp[value_col].values for _, grp in df.groupby(group_col)]
    f, p = stats.f_oneway(*groups)
    return {'f_statistic': round(f, 4), 'p_value': round(p, 6),
            'significant': p < 0.05}


# ─── VISUALISATION HELPERS ────────────────────────────────────────────────────

CITY_PALETTE = [
    '#1a6ea8', '#e84545', '#2ecc71', '#f39c12', '#9b59b6',
    '#1abc9c', '#e67e22', '#e74c3c', '#3498db', '#95a5a6'
]


def get_city_palette(cities) -> dict:
    """Map city names to hex colours."""
    return dict(zip(cities, CITY_PALETTE[:len(cities)]))


def plot_temp_trends(df: pd.DataFrame, save_path: str = None):
    """Line chart of annual average temperatures."""
    city_pal = get_city_palette(df['city'].unique())
    yearly   = df.groupby(['city', 'year'])['temp_avg_c'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(14, 6))
    for city, grp in yearly.groupby('city'):
        ax.plot(grp['year'], grp['temp_avg_c'], marker='o',
                linewidth=2.2, label=city, color=city_pal[city])
    ax.set_title('Annual Average Temperature Trends', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year'); ax.set_ylabel('Avg Temperature (°C)')
    ax.legend(ncol=5, fontsize=9, loc='upper center', bbox_to_anchor=(0.5, -0.18))
    ax.grid(alpha=0.4)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_monthly_heatmap(df: pd.DataFrame, save_path: str = None):
    """Monthly temperature heatmap."""
    pivot = df.groupby(['city', 'month'])['temp_avg_c'].mean().unstack()
    pivot.columns = ['Jan','Feb','Mar','Apr','May','Jun',
                     'Jul','Aug','Sep','Oct','Nov','Dec']
    fig, ax = plt.subplots(figsize=(13, 6))
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='RdYlBu_r',
                linewidths=0.5, ax=ax, cbar_kws={'label': 'Avg Temp (°C)'})
    ax.set_title('Monthly Temperature Heatmap', fontsize=14, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
