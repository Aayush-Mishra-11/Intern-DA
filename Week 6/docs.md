# Interactive Sales Dashboard

## Project Overview

This dashboard visualizes sales data to understand trends, customer segments, and product performance. It uses Seaborn and Matplotlib for static charts.

**Goals:**
- Analyze sales trends over time
- Understand product performance
- Identify customer segments by region
- Create interactive dashboard for business insights

## Files Included

```
Week 6/
├── dashboard.ipynb       # Step-by-step tutorial
├── dashboard.py         # Main Python script
├── requirements.txt     # Python dependencies
├── sales_data.csv      # Sales dataset (100 rows)
├── visualizations/     # Saved chart images
├── docs.md            # This documentation
└── demo.py            # Quick demo script
```

## Setup Instructions

1. Install Python (version 3.8 or higher)

2. Install required packages:    pip install -r requirements.txt

3. Run the dashboard:            python dashboard.py

4. Open the notebook:            jupyter notebook dashboard.ipynb

## Chart Guide

### 1. Sales Trend (Line Chart)
Shows daily sales over time. Look for patterns - are sales growing or declining?

### 2. Price Distribution (Box Plot)
Displays price ranges for each product. The box shows middle 50% of prices, lines show min/max.

### 3. Sales by Region (Bar Chart)
Compares total sales across 4 regions: East, West, North, South.

### 4. Quantity Distribution (Violin Plot)
Shows how quantities vary for each product - wider means more common values.

### 5. Correlation Heatmap
Shows relationships between Quantity, Price, and Total Sales.
- Values near 1 = strong positive relationship
- Values near -1 = strong negative relationship

### 6. Product Distribution (Pie Chart)
Shows what percentage of total sales comes from each product.

## How to Use

Run individual chart functions:
```python
from dashboard import plot_sales_trend
plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Total_Sales'], marker='o', markersize=4)
plt.title('Daily Sales Trend')
plt.show()
```

Or open `dashboard.ipynb` for a step-by-step walkthrough.

## Data Summary

- 100 sales records
- 5 products: Phone, Laptop, Tablet, Monitor, Headphones
- 4 regions: East, West, North, South
- Date range: January to April 2024

---

## Quality Standards Checklist

### Project Overview
- Clear description of project goals and objectives
- Business context and problem statement

### Setup Instructions
- Step-by-step installation and configuration guide
- All dependencies listed

### Code Structure
- Well-organized code with clear file hierarchy
- Functions for each chart type
- Separate static and interactive visualizations

### Visual Documentation
- Screenshots demonstrating functionality
- All 5+ chart types included
- Professional color scheme

### Technical Details

**Libraries Used:**
- pandas: Data loading and manipulation
- matplotlib: Basic plotting
- seaborn: Statistical visualizations (box plots, violin plots, heatmaps)

**Chart Types:**
1. Line Chart - Daily sales trend
2. Box Plot - Price distribution by product
3. Bar Chart - Sales by region
4. Violin Plot - Quantity distribution
5. Heatmap - Correlation matrix
6. Pie Chart - Product sales share
7. Subplot Grid - Combined dashboard

**Data Processing:**
- Date conversion to datetime
- Groupby operations for aggregation
- Correlation calculation

### Testing Evidence

Run these commands to verify:
```bash
# Test 1: Check data loads
python -c "import pandas as pd; df = pd.read_csv('sales_data.csv'); print(f'Records: {len(df)}')"

# Test 2: Run dashboard
python dashboard.py

# Test 3: Check visualizations folder
ls visualizations/
```

Expected output: 7 PNG files in visualizations/

---

## Technical Architecture

### Functions in dashboard.py

| Function | Description |
|----------|-------------|
| plot_sales_trend() | Line chart with Matplotlib |
| plot_product_boxplot() | Box plot with Seaborn |
| plot_region_sales() | Bar chart with Matplotlib |
| plot_quantity_violin() | Violin plot with Seaborn |
| plot_correlation_heatmap() | Heatmap with Seaborn |
| plot_product_pie() | Pie chart with Matplotlib |
| plot_strip() | Strip plot with Seaborn |
| create_dashboard() | Combined subplot dashboard |

### Color Scheme

| Color | Hex | Usage |
|-------|-----|-------|
| Primary | #2E86AB | Main charts |
| Secondary | #A23B72 | Secondary elements |
| Accent | #F18F01 | Highlights |
| Success | #C73E1D | Warnings |

---

