<div align="center">

# 🌦️ Global Weather Data Analysis
### Project 3 — Weather & Climate Domain

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557C?style=for-the-badge)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-4EACC5?style=for-the-badge)](https://seaborn.pydata.org/)

---

**Author** · Binal Doshi &nbsp;|&nbsp; MSc Artificial Intelligence & Data Science &nbsp;|&nbsp; University of Mumbai (2025–2027)

</div>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Repository Structure](#-repository-structure)
- [Setup & Installation](#-setup--installation)
- [Analysis Workflow](#-analysis-workflow)
- [Visualizations](#-visualizations)
- [Statistical Analysis](#-statistical-analysis)
- [Key Findings & Business Insights](#-key-findings--business-insights)
- [Technologies Used](#-technologies-used)
- [File Descriptions](#-file-descriptions)
- [How to Contribute](#-how-to-contribute)
- [License](#-license)

---

## 📌 Project Overview

This project is a **comprehensive Exploratory Data Analysis (EDA)** of daily historical weather records from **10 major global cities** spanning **6 years (2018–2023)**. It forms the third component of a five-project Multi-Domain Data Analysis Portfolio built as part of a structured Python & Data Science curriculum.

The analysis answers real-world questions across three themes:

| Theme | Questions Explored |
|---|---|
| 🌡️ **Temperature** | How do temperatures trend year-on-year? Which cities are hottest/coldest? What is the seasonal spread? |
| 🌧️ **Rainfall** | Which cities receive the most rain? When does monsoon peak? How does rainfall vary by season? |
| ⚡ **Extreme Events** | Which cities experience the most extreme heat, heavy rain, or frost? How do variables correlate? |

### Scope at a Glance

| Attribute | Value |
|---|---|
| Dataset Size | 21,910 rows × 15 columns |
| Cities Covered | 10 global cities across 6 continents |
| Time Period | January 2018 – December 2023 |
| Visualizations | 10 professional charts (all chart types) |
| Statistical Tests | 3 hypothesis tests (t-test, ANOVA, Pearson r) |
| Notebook Cells | 16 structured cells across 8 sections |

---

## 📦 Dataset

### Source
The dataset (`global_weather_2018_2023.csv`) was modelled on real meteorological patterns from publicly available sources including **Kaggle's Global Weather Repository** and **NOAA Historical Climate Normals**. It simulates realistic daily readings across 10 cities based on verified climatic profiles.

> 📥 **Kaggle Reference:** [Global Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository)

### Cities & Climate Types

| City | Country | Climate Type | Avg Temp (°C) | Annual Rain (mm) |
|---|---|---|---|---|
| 🇮🇳 Mumbai | India | Tropical Wet-Dry | 28–30 | ~880 |
| 🇮🇳 Delhi | India | Semi-Arid | 25–28 | ~450 |
| 🇬🇧 London | United Kingdom | Temperate Oceanic | 12–14 | ~620 |
| 🇺🇸 New York | USA | Humid Continental | 14–16 | ~580 |
| 🇯🇵 Tokyo | Japan | Humid Subtropical | 16–18 | ~680 |
| 🇦🇺 Sydney | Australia | Oceanic/Subtropical | 18–20 | ~510 |
| 🇦🇪 Dubai | UAE | Hot Desert | 32–34 | ~75 |
| 🇷🇺 Moscow | Russia | Humid Continental | 5–8 | ~520 |
| 🇸🇬 Singapore | Singapore | Tropical Rainforest | 27–29 | ~1,095 |
| 🇪🇬 Cairo | Egypt | Hot Desert | 22–24 | ~73 |

### Column Reference

| Column | Data Type | Unit | Description |
|---|---|---|---|
| `city` | String | — | City name |
| `country` | String | — | Country name |
| `date` | Date | YYYY-MM-DD | Daily record date |
| `latitude` | Float | degrees | Geographic latitude |
| `longitude` | Float | degrees | Geographic longitude |
| `temp_max_c` | Float | °C | Daily maximum temperature |
| `temp_min_c` | Float | °C | Daily minimum temperature |
| `temp_avg_c` | Float | °C | Daily average temperature |
| `precipitation_mm` | Float | mm | Daily rainfall / precipitation |
| `humidity_pct` | Float | % | Relative humidity (0–100) |
| `wind_speed_kmh` | Float | km/h | Daily wind speed |
| `pressure_hpa` | Float | hPa | Atmospheric pressure |
| `uv_index` | Float | 0–11+ | UV radiation index |
| `visibility_km` | Float | km | Atmospheric visibility |
| `weather_condition` | String | — | Categorical label (Clear/Sunny, Rain, Heavy Rain, Cloudy, Extreme Heat, Snow/Frost) |

---

## 📁 Repository Structure

```
weather_portfolio/
│
├── 📄 README.md                              ← Project overview and navigation (you are here)
├── 📄 requirements.txt                       ← All Python dependencies with versions
│
├── 📂 data/
│   └── global_weather_2018_2023.csv         ← Main dataset · 21,910 rows × 15 cols
│
├── 📂 notebooks/
│   └── weather_analysis.ipynb               ← Full analysis notebook · 16 cells · 8 sections
│
├── 📂 src/
│   └── weather_utils.py                     ← Reusable utility functions module
│
├── 📂 visualizations/
│   ├── viz1_annual_temp_trends.png          ← Line chart: annual avg temp per city
│   ├── viz2_monthly_temp_heatmap.png        ← Heatmap: monthly temps by city
│   ├── viz3_annual_rainfall_bar.png         ← Bar chart: average annual rainfall
│   ├── viz4_seasonal_rainfall.png           ← Subplots: seasonal rainfall per city
│   ├── viz5_temp_boxplot.png                ← Box plot: temperature distribution
│   ├── viz6_humidity_rainfall_scatter.png   ← Scatter: humidity vs precipitation
│   ├── viz7_extreme_weather_events.png      ← Grouped bar: extreme event counts
│   ├── viz8_yearly_rainfall_trend.png       ← Line chart: year-on-year rainfall
│   ├── viz9_correlation_heatmap.png         ← Heatmap: 9-variable correlation matrix
│   └── viz10_wind_speed_distribution.png    ← KDE plot: wind speed distribution
│
├── 📂 reports/
│   └── weather_analysis_report.pdf          ← Auto-generated PDF executive report
│
├── 📂 docs/
│   └── Weather_Analysis_Documentation.docx ← Full Word documentation (6 sections)
│
└── 📂 presentation/
    └── weather_analysis_slides.pptx         ← Presentation slide deck
```

---

## 🚀 Setup & Installation

### Prerequisites

Make sure you have the following installed before proceeding:

- Python **3.10 or higher** — [Download](https://www.python.org/downloads/)
- pip (comes with Python)
- Git — [Download](https://git-scm.com/downloads/)
- Jupyter Notebook or JupyterLab

---

### Step-by-Step Installation

**1. Clone the repository**

```bash
git clone https://github.com/Binal2004/weather-analysis-portfolio.git
cd weather-analysis-portfolio
```

**2. (Recommended) Create a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install all dependencies**

```bash
pip install -r requirements.txt
```

> ⚠️ If you face issues with matplotlib on macOS, run: `pip install matplotlib --upgrade`

**4. Launch the Jupyter notebook**

```bash
jupyter notebook notebooks/weather_analysis.ipynb
```

**5. Run the full analysis**

Once the notebook opens in your browser:
- Click **Kernel → Restart & Run All**
- All outputs, charts, and print statements will generate automatically
- 10 PNG visualizations will be saved to the `visualizations/` folder

---

### Dependencies (`requirements.txt`)

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
jupyter>=1.0.0
notebook>=7.0.0
openpyxl>=3.1.0
```

---

## 🔬 Analysis Workflow

The notebook is organized into **8 logical sections** across 16 cells:

```
Section 1 · Imports & Setup
    └─ Library imports, theme configuration, seaborn whitegrid setup

Section 2 · Data Loading & Exploration
    └─ CSV load with parse_dates, feature engineering (year / month / season columns)
    └─ Shape, dtypes, value counts, first/last rows

Section 3 · Data Quality Check
    └─ Missing value audit per column
    └─ Duplicate detection
    └─ Descriptive statistics (mean, std, min, max, quartiles)

Section 4 · Data Cleaning & Validation
    └─ Physical range validation (temp_max >= temp_min, rain >= 0, humidity 0–100)
    └─ Per-city summary statistics table

Section 5 · Temperature Analysis         → VIZ 1, VIZ 2, VIZ 5
    └─ Annual average temperature trends (2018–2023)
    └─ Monthly temperature heatmap
    └─ Temperature distribution box plots (sorted by mean)

Section 6 · Rainfall Analysis            → VIZ 3, VIZ 4, VIZ 8
    └─ Average annual rainfall bar chart (annotated values)
    └─ Seasonal rainfall subplots (Spring / Summer / Autumn / Winter)
    └─ Year-on-year total rainfall trend lines

Section 7 · Extreme Weather & Correlations → VIZ 6, VIZ 7, VIZ 9, VIZ 10
    └─ Extreme weather event counts (Heavy Rain, Extreme Heat, Snow/Frost)
    └─ 9-variable Pearson correlation heatmap
    └─ Humidity vs Precipitation scatter with regression line
    └─ Wind speed KDE distribution curves

Section 8 · Statistical Hypothesis Testing & Summary
    └─ t-test: Mumbai monsoon vs non-monsoon rainfall
    └─ Pearson r: Temperature vs UV Index
    └─ One-way ANOVA: city temperature differences
    └─ Final project summary statistics
```

---

## 📊 Visualizations

All 10 charts are saved at **150 DPI** with consistent styling — same colour per city across every chart.

| # | Chart | Type | Business Question |
|---|---|---|---|
| 1 | `viz1_annual_temp_trends.png` | Multi-line | How do temperatures trend per city year-on-year? |
| 2 | `viz2_monthly_temp_heatmap.png` | Heatmap | Which months are hottest and coldest per city? |
| 3 | `viz3_annual_rainfall_bar.png` | Annotated bar | Which city receives the most/least annual rain? |
| 4 | `viz4_seasonal_rainfall.png` | Subplot bar grid (2×5) | How is rainfall spread across seasons? |
| 5 | `viz5_temp_boxplot.png` | Box plot | What is the temperature IQR and spread per city? |
| 6 | `viz6_humidity_rainfall_scatter.png` | Scatter + regression | Does higher humidity predict more rainfall? |
| 7 | `viz7_extreme_weather_events.png` | Grouped bar | How many extreme event days per city per type? |
| 8 | `viz8_yearly_rainfall_trend.png` | Multi-line | Do annual rainfall totals trend up or down? |
| 9 | `viz9_correlation_heatmap.png` | Correlation matrix | How do all 9 weather variables relate? |
| 10 | `viz10_wind_speed_distribution.png` | KDE density | How is wind speed distributed across cities? |

### Design Standards Applied
- Seaborn `whitegrid` theme with `DejaVu Sans` font throughout
- 10-colour city palette — **consistent across every multi-city chart**
- All axes labeled with units (°C, mm, km/h, %)
- All charts include: bold title, axis labels, legend, alpha-0.4 gridlines
- `bbox_inches='tight'` on all saves to prevent label clipping

---

## 📐 Statistical Analysis

### Hypothesis Test 1 — Mumbai Monsoon Rainfall (t-test)

```
H₀: Mean daily rainfall in monsoon months (Jun–Sep) = non-monsoon months
H₁: Monsoon months receive significantly more rainfall

Result : t ≈ 8.4 | p < 0.001 → REJECT H₀
Finding: Mumbai's monsoon months receive ~72% of the city's annual rainfall
```

### Hypothesis Test 2 — Temperature vs UV Index (Pearson Correlation)

```
H₀: No linear relationship between temperature and UV index
H₁: Significant positive correlation exists

Result : r ≈ 0.82 | p < 0.001 → Strong positive correlation confirmed
Finding: Higher temperatures are strongly associated with higher UV radiation
```

### Hypothesis Test 3 — City Temperature Differences (One-Way ANOVA)

```
H₀: All 10 cities have the same mean temperature
H₁: At least one city has a significantly different mean

Result : F >> 1 | p < 0.001 → REJECT H₀
Finding: Cities across different climate zones have significantly different temperature profiles
```

---

## 💡 Key Findings & Business Insights

### Top-Line Statistics

| Metric | Value | City |
|---|---|---|
| 🔥 Hottest annual average | ~32°C | Dubai |
| 🧊 Coldest annual average | ~6°C | Moscow |
| 🌧️ Wettest city | ~1,095 mm/yr | Singapore |
| 🏜️ Driest city | ~73 mm/yr | Cairo |
| ❄️ Most snow/frost days | 180+ days/yr | Moscow |
| ☀️ Highest UV risk | 11+ index | Dubai & Singapore |
| 🌬️ Strongest temp–UV link | r = 0.82 | Global dataset |
| ⛈️ Monsoon significance | p < 0.001 | Mumbai Jun–Sep |

### Business Recommendations

1. **Urban Planning & Infrastructure** — Moscow and New York experience 100+ frost/snow days annually; investment in winter road maintenance, heating systems, and pipe insulation is essential.

2. **Agriculture & Food Security** — Mumbai's annual rainfall is concentrated in just 4 months (Jun–Sep). Crop planning, reservoir management, and irrigation infrastructure must account for this extreme seasonal skew.

3. **Tourism Strategy** — London and Sydney offer the most temperate and predictable weather year-round, making them lower-risk destinations for all-season tourism campaigns compared to climate-extreme cities.

4. **Renewable Energy (Solar)** — Dubai's UV index consistently exceeds 10 for 8+ months/year. This makes it one of the most favorable cities globally for large-scale solar panel deployment.

5. **Flood Risk Management** — Singapore and Mumbai exceed 10mm/day rainfall events multiple times per year. Robust urban drainage systems and flood early-warning systems are critical priorities.

6. **Occupational Health** — High humidity (>80%) combined with temperatures above 28°C (Singapore, Mumbai) creates significant heat stress risk for outdoor workers; heat advisory protocols are recommended.

---

## 🛠️ Technologies Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Core programming language |
| pandas | ≥2.0.0 | Data loading, manipulation, groupby, aggregation |
| numpy | ≥1.24.0 | Array operations, masking, numerical computing |
| matplotlib | ≥3.7.0 | Core plotting engine — figures, axes, saving |
| seaborn | ≥0.12.0 | Statistical charts: heatmap, boxplot, KDE, scatter |
| scipy | ≥1.10.0 | `linregress`, `pearsonr`, `ttest_ind`, `f_oneway` |
| Jupyter Notebook | ≥7.0.0 | Interactive analysis environment |
| openpyxl | ≥3.1.0 | Excel export support |

---

## 📄 File Descriptions

| File | Description |
|---|---|
| `notebooks/weather_analysis.ipynb` | Main analysis notebook — 16 cells, fully documented with markdown explanations and inline insights |
| `data/global_weather_2018_2023.csv` | Dataset — 21,910 daily weather records for 10 cities from 2018–2023 |
| `src/weather_utils.py` | Utility module — 10 reusable functions for loading, validating, aggregating, and plotting weather data |
| `docs/Weather_Analysis_Documentation.docx` | Full project documentation — covers Project Overview, Setup, Code Structure, Visual Docs, Technical Details, and Testing Evidence |
| `requirements.txt` | Pinned Python dependencies for reproducible environment setup |
| `visualizations/*.png` | 10 exported chart PNGs at 150 DPI, ready for reports and presentations |

---

## 🤝 How to Contribute

Contributions and suggestions are welcome! Here's how:

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/add-climate-forecast`
3. Commit your changes: `git commit -m "Add climate forecasting section"`
4. Push to the branch: `git push origin feature/add-climate-forecast`
5. Open a Pull Request

**Possible extensions:**
- Add time-series forecasting (ARIMA / Prophet) for temperature predictions
- Integrate real-time weather API data (OpenWeatherMap)
- Build an interactive Streamlit dashboard
- Expand to 20+ cities for broader global coverage

---

## 📬 Contact

**Binal Doshi**
- 📧 Email: [binaldoshi04@gmail.com](mailto:binaldoshi04@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/binal-doshi-2005abc](https://linkedin.com/in/binal-doshi-2005abc)
- 🐙 GitHub: [github.com/Binal2004](https://github.com/Binal2004)

---

## 📜 License

This project is part of an academic portfolio. Dataset is modelled on open-source meteorological data for educational purposes.

---

<div align="center">

⭐ If you found this project useful, please consider starring the repository!

</div>
