# Tips Data Analysis

A mini exploratory data analysis project using the `tips` dataset from seaborn.

## Overview

This project demonstrates basic EDA with pandas and seaborn including data summary, feature engineering, grouping, and visualizations.

## What the script does

In `main.py`, the script:

- Loads seaborn's `tips` dataset
- Prints first 5 rows and dataset shape
- Displays descriptive statistics and missing values
- Adds `tip_percent` = (tip / total_bill) * 100
- Calculates average tip by gender, day, and smoker status
- Plots:
  - Histogram of total bill
  - Scatter plot of total bill vs tip
  - Bar chart of average tip by day
  - Correlation heatmap for `total_bill`, `tip`, and `size`

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn

## Installation

```bash
python -m pip install pandas numpy matplotlib seaborn
```

## Usage

```bash
python main.py
```

## Notes

- The dataset is loaded directly from seaborn; no local data file is needed.
- This is intended as a quick EDA demonstration, not a production pipeline.

