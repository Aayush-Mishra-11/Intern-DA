""" Sales Dashboard """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the sales data
df = pd.read_csv('D:\\Things\\Documents\\Internship\\The Developer Arena\\Week 6\\sales_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set a cohesive color scheme
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6B4C9A']

# Set seaborn style
sns.set_style('whitegrid')


# CHART 1: Sales Over Time (Line Chart)
def plot_sales_trend():
    """Show sales trend over time"""
    plt.figure(figsize=(12, 5))
    plt.plot(df['Date'], df['Total_Sales'], marker='o', markersize=4, color='#2E86AB')
    plt.title('Daily Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# CHART 2: Sales by Product Category (Box Plot)
def plot_product_boxplot():
    """Show price distribution by product category"""
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='Product', y='Price', hue='Product', data=df, palette='Set2', legend=False)
    plt.title('Price Distribution by Product')
    plt.xlabel('Product')
    plt.ylabel('Price ($)')
    plt.tight_layout()
    plt.show()


# CHART 3: Sales by Region (Bar Chart)
def plot_region_sales():
    """Show total sales by region"""
    plt.figure(figsize=(10, 5))
    region_sales = df.groupby('Region')['Total_Sales'].sum()
    region_sales.plot(kind='bar', color=colors[:4])
    plt.title('Total Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# CHART 4: Quantity Distribution (Violin Plot)
def plot_quantity_violin():
    """Show quantity distribution by product"""
    plt.figure(figsize=(10, 5))
    sns.violinplot(x='Product', y='Quantity', hue='Product', data=df, palette='Set3', legend=False)
    plt.title('Quantity Distribution by Product')
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.tight_layout()
    plt.show()


# CHART 5: Correlation Heatmap
def plot_correlation_heatmap():
    """Show correlation between numerical variables"""
    plt.figure(figsize=(8, 6))
    numeric_cols = ['Quantity', 'Price', 'Total_Sales']
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='RdBu_r', fmt='.2f', square=True)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()


# CHART 6: Product Performance (Pie Chart)
def plot_product_pie():
    """Show sales distribution by product"""
    plt.figure(figsize=(8, 8))
    product_sales = df.groupby('Product')['Total_Sales'].sum()
    product_sales.plot(kind='pie', autopct='%1.1f%%', colors=colors)
    plt.title('Sales Distribution by Product')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()


# CHART 7: Strip Plot
def plot_strip():
    """Show individual data points"""
    plt.figure(figsize=(10, 5))
    sns.stripplot(x='Product', y='Total_Sales', hue='Product', data=df, palette='Set2', legend=False)
    plt.title('Individual Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales ($)')
    plt.tight_layout()
    plt.show()

# MAIN: Generate all charts and save
if __name__ == '__main__':
    print('Generating Sales Dashboard...')

    # Create visualizations folder
    os.makedirs('visualizations', exist_ok=True)

    # Chart 1: Sales trend
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(df['Date'], df['Total_Sales'], marker='o', color='#2E86AB', markersize=4)
    ax1.set_title('Daily Sales Trend')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/sales_trend.png', dpi=150)
    plt.close()

    # Chart 2: Box plot
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='Product', y='Price', hue='Product', data=df, ax=ax2, palette='Set2', legend=False)
    ax2.set_title('Price Distribution by Product')
    plt.tight_layout()
    plt.savefig('visualizations/price_boxplot.png', dpi=150)
    plt.close()

    # Chart 3: Region bar chart
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    region_data = df.groupby('Region')['Total_Sales'].sum()
    region_data.plot(kind='bar', ax=ax3, color=colors[:4])
    ax3.set_title('Total Sales by Region')
    ax3.set_xlabel('Region')
    ax3.set_ylabel('Sales ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('visualizations/region_sales.png', dpi=150)
    plt.close()

    # Chart 4: Correlation heatmap
    fig4, ax4 = plt.subplots(figsize=(8, 6))
    numeric_df = df[['Quantity', 'Price', 'Total_Sales']]
    sns.heatmap(numeric_df.corr(), annot=True, cmap='RdBu_r', ax=ax4, fmt='.2f')
    ax4.set_title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('visualizations/correlation_heatmap.png', dpi=150)
    plt.close()

    # Chart 5: Violin plot
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    sns.violinplot(x='Product', y='Quantity', hue='Product', data=df, ax=ax5, palette='Set3', legend=False)
    ax5.set_title('Quantity Distribution by Product')
    plt.tight_layout()
    plt.savefig('visualizations/quantity_violin.png', dpi=150)
    plt.close()

    # Chart 6: Product pie chart
    fig6, ax6 = plt.subplots(figsize=(8, 8))
    product_data = df.groupby('Product')['Total_Sales'].sum()
    product_data.plot(kind='pie', ax=ax6, autopct='%1.1f%%', colors=colors)
    ax6.set_title('Sales Distribution by Product')
    ax6.set_ylabel('')
    plt.tight_layout()
    plt.savefig('visualizations/product_pie.png', dpi=150)
    plt.close()

    # Create subplot grid (2x2)
    fig7, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig7.suptitle('Sales Dashboard - Multi-Plot Layout', fontsize=16, fontweight='bold')

    # Subplot 1: Sales trend
    axes[0, 0].plot(df['Date'], df['Total_Sales'], marker='o', color='#2E86AB', markersize=3)
    axes[0, 0].set_title('Daily Sales Trend')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Sales ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)

    # Subplot 2: Box plot
    sns.boxplot(x='Product', y='Price', hue='Product', data=df, ax=axes[0, 1], palette='Set2', legend=False)
    axes[0, 1].set_title('Price Distribution')
    axes[0, 1].tick_params(axis='x', rotation=45)

    # Subplot 3: Region bar
    region_data.plot(kind='bar', ax=axes[1, 0], color='#A23B72')
    axes[1, 0].set_title('Sales by Region')
    axes[1, 0].set_xlabel('Region')
    axes[1, 0].set_ylabel('Sales ($)')
    axes[1, 0].tick_params(axis='x', rotation=0)

    # Subplot 4: Heatmap
    sns.heatmap(numeric_df.corr(), annot=True, cmap='RdBu_r', ax=axes[1, 1], fmt='.2f')
    axes[1, 1].set_title('Correlation Heatmap')

    plt.tight_layout()
    plt.savefig('visualizations/dashboard_grid.png', dpi=150)
    plt.close()

    print('Static charts saved to visualizations/')
    print('Done!')
