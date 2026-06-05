# 🌦️ Project 3 — Global Weather Data Analysis
**Multi-Domain Data Analysis Portfolio | Weather & Climate Domain**

> **Author:** Binal Doshi | MSc AI & Data Science, University of Mumbai (2025–2027)  
> **Dataset:** Global Weather Repository — 10 Cities × 6 Years (21,910 records)  
> **Tools:** Python · Pandas · Matplotlib · Seaborn · SciPy  

---

## 📌 Project Overview

This project performs comprehensive exploratory data analysis on historical weather data from 10 major global cities (2018–2023). The analysis covers temperature trends, rainfall distribution, seasonal climate patterns, extreme weather events, and inter-variable correlations — generating 10 professional visualizations and 3 statistical hypothesis tests.

---

## 📁 Repository Structure

```
weather_portfolio/
├── README.md                          ← You are here
├── requirements.txt                   ← Python dependencies
├── data/
│   └── global_weather_2018_2023.csv  ← Main dataset (21,910 rows × 15 cols)
├── notebooks/
│   └── weather_analysis.ipynb        ← Main analysis notebook
├── reports/                           ← PDF executive report (auto-generated)
├── src/
│   └── weather_utils.py              ← Reusable utility functions
├── visualizations/                    ← 10 PNG charts
│   ├── viz1_annual_temp_trends.png
│   ├── viz2_monthly_temp_heatmap.png
│   ├── viz3_annual_rainfall_bar.png
│   ├── viz4_seasonal_rainfall.png
│   ├── viz5_temp_boxplot.png
│   ├── viz6_humidity_rainfall_scatter.png
│   ├── viz7_extreme_weather_events.png
│   ├── viz8_yearly_rainfall_trend.png
│   ├── viz9_correlation_heatmap.png
│   └── viz10_wind_speed_distribution.png
├── presentation/                      ← Slide deck assets
└── docs/                              ← Detailed project documentation
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Binal2004/weather-analysis-portfolio.git
cd weather-analysis-portfolio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch notebook
jupyter notebook notebooks/weather_analysis.ipynb
```

---

## 📊 Key Findings

| Metric | Value | City |
|--------|-------|------|
| Hottest annual avg | 32.1°C | Dubai |
| Coldest annual avg | 5.8°C | Moscow |
| Highest annual rain | ~1,095mm | Singapore |
| Lowest annual rain | ~73mm | Cairo |
| Most snow/frost days | 180+ days/yr | Moscow |
| Highest UV index | 11+ | Dubai & Singapore |

---

## 🔬 Analysis Highlights

- **Temperature Analysis** — Annual trends, monthly heatmap, seasonal box plots across 10 cities
- **Rainfall Patterns** — Annual totals, seasonal distribution, 6-year trend lines
- **Extreme Weather** — Heavy rain, extreme heat, snow/frost event counts per city
- **Correlations** — 9-variable Pearson correlation matrix; humidity vs rainfall scatter
- **Statistics** — t-test (monsoon significance), ANOVA (city temperature differences), Pearson r

---

## 📦 Dataset Columns

| Column | Description |
|--------|-------------|
| `city`, `country` | Location identifiers |
| `date` | Daily record (2018-01-01 to 2023-12-31) |
| `temp_max_c`, `temp_min_c`, `temp_avg_c` | Daily temperature readings |
| `precipitation_mm` | Daily rainfall |
| `humidity_pct` | Relative humidity |
| `wind_speed_kmh` | Daily wind speed |
| `pressure_hpa` | Atmospheric pressure |
| `uv_index` | UV radiation level |
| `visibility_km` | Atmospheric visibility |
| `weather_condition` | Categorical condition label |

---

*Part of the Month 2 — Data Analysis & Visualization Expertise curriculum*
