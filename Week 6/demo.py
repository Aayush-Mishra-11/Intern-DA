"""
Demo script to show how to use the dashboard
Run this to see all the charts in action
"""

# To create animated GIF, uncomment the following:
# Note: GIF generation requires imageio or can be done manually

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('D:\\Things\\Documents\\Internship\\The Developer Arena\\Week 6\\sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("\nSALES DASHBOARD DEMO")
print("-" * 50)
print("\nThis script shows quick data summary.\n")

# Quick stats
print("DATA SUMMARY:")
print(f"- Total records: {len(df)}")
print(f"- Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"- Total sales: ${df['Total_Sales'].sum():,.0f}")
print(f"- Products: {', '.join(df['Product'].unique())}")
print(f"- Regions: {', '.join(df['Region'].unique())}")

print("\nSALES BY PRODUCT:")
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
for product, sales in product_sales.items():
    print(f"  {product}: ${sales:,.0f}")

print("\nSALES BY REGION:")
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
for region, sales in region_sales.items():
    print(f"  {region}: ${sales:,.0f}")

print("\nTo see interactive charts, open dashboard.ipynb")
print("or run: python dashboard.py\n")
