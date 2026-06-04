import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load datasets
churn_df = pd.read_csv('customer_churn.csv')
sales_df = pd.read_csv('sales_data.csv')

plt.style.use('seaborn-v0_8-whitegrid')

# Figure 1: Distribution plots for Churn data
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Distribution Analysis - Customer Churn Data', fontsize=14, fontweight='bold')

axes[0, 0].hist(churn_df['Tenure'], bins=30, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 0].axvline(churn_df['Tenure'].mean(), color='red', linestyle='--', label=f"Mean: {churn_df['Tenure'].mean():.1f}")
axes[0, 0].axvline(churn_df['Tenure'].median(), color='green', linestyle='--', label=f"Median: {churn_df['Tenure'].median():.1f}")
axes[0, 0].set_title('Tenure Distribution')
axes[0, 0].set_xlabel('Tenure (months)')
axes[0, 0].legend()

axes[0, 1].hist(churn_df['MonthlyCharges'], bins=30, edgecolor='black', alpha=0.7, color='coral')
axes[0, 1].axvline(churn_df['MonthlyCharges'].mean(), color='red', linestyle='--', label=f"Mean: {churn_df['MonthlyCharges'].mean():.1f}")
axes[0, 1].axvline(churn_df['MonthlyCharges'].median(), color='green', linestyle='--', label=f"Median: {churn_df['MonthlyCharges'].median():.1f}")
axes[0, 1].set_title('Monthly Charges Distribution')
axes[0, 1].set_xlabel('Monthly Charges ($)')
axes[0, 1].legend()

axes[0, 2].hist(churn_df['TotalCharges'], bins=30, edgecolor='black', alpha=0.7, color='mediumseagreen')
axes[0, 2].axvline(churn_df['TotalCharges'].mean(), color='red', linestyle='--', label=f"Mean: {churn_df['TotalCharges'].mean():.1f}")
axes[0, 2].axvline(churn_df['TotalCharges'].median(), color='green', linestyle='--', label=f"Median: {churn_df['TotalCharges'].median():.1f}")
axes[0, 2].set_title('Total Charges Distribution')
axes[0, 2].set_xlabel('Total Charges ($)')
axes[0, 2].legend()

sns.kdeplot(data=churn_df['Tenure'], ax=axes[1, 0], fill=True, color='steelblue')
axes[1, 0].set_title('Tenure Density Plot')

sns.kdeplot(data=churn_df['MonthlyCharges'], ax=axes[1, 1], fill=True, color='coral')
axes[1, 1].set_title('Monthly Charges Density Plot')

sns.kdeplot(data=churn_df['TotalCharges'], ax=axes[1, 2], fill=True, color='mediumseagreen')
axes[1, 2].set_title('Total charges Density Plot')

plt.tight_layout()
plt.savefig('distribution_churn.png', dpi=150, bbox_inches='tight')
plt.close()
print('Created: distribution_churn.png')

# Figure 2: Distribution plots for Sales data
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Distribution Analysis - Sales Data', fontsize=14, fontweight='bold')

axes[0, 0].hist(sales_df['Quantity'], bins=20, edgecolor='black', alpha=0.7, color='purple')
axes[0, 0].axvline(sales_df['Quantity'].mean(), color='red', linestyle='--', label=f"Mean: {sales_df['Quantity'].mean():.1f}")
axes[0, 0].set_title('Quantity Distribution')
axes[0, 0].set_xlabel('Quantity')
axes[0, 0].legend()

axes[0, 1].hist(sales_df['Price'], bins=20, edgecolor='black', alpha=0.7, color='orange')
axes[0, 1].axvline(sales_df['Price'].mean(), color='red', linestyle='--', label=f"Mean: {sales_df['Price'].mean():.1f}")
axes[0, 1].set_title('Price Distribution')
axes[0, 1].set_xlabel('Price ($)')
axes[0, 1].legend()

axes[0, 2].hist(sales_df['Total_Sales'], bins=20, edgecolor='black', alpha=0.7, color='teal')
axes[0, 2].axvline(sales_df['Total_Sales'].mean(), color='red', linestyle='--', label=f"Mean: {sales_df['Total_Sales'].mean():.1f}")
axes[0, 2].set_title('Total Sales Distribution')
axes[0, 2].set_xlabel('Total Sales ($)')
axes[0, 2].legend()

sns.kdeplot(data=sales_df['Quantity'], ax=axes[1, 0], fill=True, color='purple')
axes[1, 0].set_title('Quantity Density Plot')

sns.kdeplot(data=sales_df['Price'], ax=axes[1, 1], fill=True, color='orange')
axes[1, 1].set_title('Price Density Plot')

sns.kdeplot(data=sales_df['Total_Sales'], ax=axes[1, 2], fill=True, color='teal')
axes[1, 2].set_title('Total Sales Density Plot')

plt.tight_layout()
plt.savefig('distribution_sales.png', dpi=150, bbox_inches='tight')
plt.close()
print('Created: distribution_sales.png')

# Figure 3: Correlation heatmaps
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

churn_numeric = churn_df[['Tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']]
pearson_corr = churn_numeric.corr(method='pearson')
spearman_corr = churn_numeric.corr(method='spearman')

sns.heatmap(pearson_corr, annot=True, cmap='RdBu_r', center=0, fmt='.3f', ax=axes[0], vmin=-1, vmax=1)
axes[0].set_title('Pearson Correlation (Churn Data)', fontweight='bold')

sns.heatmap(spearman_corr, annot=True, cmap='RdBu_r', center=0, fmt='.3f', ax=axes[1], vmin=-1, vmax=1)
axes[1].set_title('Spearman Correlation (Churn Data)', fontweight='bold')

plt.tight_layout()
plt.savefig('correlation_churn.png', dpi=150, bbox_inches='tight')
plt.close()
print('Created: correlation_churn.png')

# Figure 4: Sales correlation heatmap
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sales_numeric = sales_df[['Quantity', 'Price', 'Total_Sales']]
pearson_sales = sales_numeric.corr(method='pearson')
spearman_sales = sales_numeric.corr(method='spearman')

sns.heatmap(pearson_sales, annot=True, cmap='Greens', center=0, fmt='.3f', ax=axes[0], vmin=0, vmax=1)
axes[0].set_title('Pearson Correlation (Sales Data)', fontweight='bold')

sns.heatmap(spearman_sales, annot=True, cmap='Greens', center=0, fmt='.3f', ax=axes[1], vmin=0, vmax=1)
axes[1].set_title('Spearman Correlation (Sales Data)', fontweight='bold')

plt.tight_layout()
plt.savefig('correlation_sales.png', dpi=150, bbox_inches='tight')
plt.close()
print('Created: correlation_sales.png')

# Figure 5: Confidence Intervals
fig, ax = plt.subplots(figsize=(12, 6))

variables = ['Tenure', 'MonthlyCharges', 'TotalCharges', 'Quantity', 'Price', 'Total_Sales']
colors = ['steelblue', 'coral', 'mediumseagreen', 'purple', 'orange', 'teal']

means = [churn_df['Tenure'].mean(), churn_df['MonthlyCharges'].mean(), churn_df['TotalCharges'].mean(),
         sales_df['Quantity'].mean(), sales_df['Price'].mean(), sales_df['Total_Sales'].mean()]

errors = []
for col in ['Tenure', 'MonthlyCharges', 'TotalCharges']:
    se = stats.sem(churn_df[col])
    me = se * stats.t.ppf(0.975, len(churn_df[col])-1)
    errors.append(me)
for col in ['Quantity', 'Price', 'Total_Sales']:
    se = stats.sem(sales_df[col])
    me = se * stats.t.ppf(0.975, len(sales_df[col])-1)
    errors.append(me)

bars = ax.bar(variables, means, yerr=errors, capsize=5, color=colors, alpha=0.7, edgecolor='black')
ax.set_ylabel('Value', fontsize=12)
ax.set_xlabel('Variable', fontsize=12)
ax.set_title('95% Confidence Intervals for Key Business Metrics', fontsize=14, fontweight='bold')
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('confidence_intervals.png', dpi=150, bbox_inches='tight')
plt.close()
print('Created: confidence_intervals.png')

# Figure 6: Regression plots
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Tenure vs TotalCharges
X1 = churn_df[['Tenure']].values
y1 = churn_df['TotalCharges'].values
model1 = LinearRegression().fit(X1, y1)
r2_1 = r2_score(y1, model1.predict(X1))

axes[0, 0].scatter(X1, y1, alpha=0.5, color='steelblue')
axes[0, 0].plot(X1, model1.predict(X1), color='red', linewidth=2)
axes[0, 0].set_xlabel('Tenure (months)')
axes[0, 0].set_ylabel('Total Charges ($)')
axes[0, 0].set_title(f'Tenure vs Total charges\nR2 = {r2_1:.4f}', fontweight='bold')

# MonthlyCharges vs TotalCharges
X2 = churn_df[['MonthlyCharges']].values
model2 = LinearRegression().fit(X2, y1)
r2_2 = r2_score(y1, model2.predict(X2))

axes[0, 1].scatter(X2, y1, alpha=0.5, color='coral')
axes[0, 1].plot(X2, model2.predict(X2), color='red', linewidth=2)
axes[0, 1].set_xlabel('Monthly Charges ($)')
axes[0, 1].set_ylabel('Total Charges ($)')
axes[0, 1].set_title(f'Monthly Charges vs Total Charges\nR2 = {r2_2:.4f}', fontweight='bold')

# Price vs Total_Sales
X3 = sales_df[['Price']].values
y3 = sales_df['Total_Sales'].values
model3 = LinearRegression().fit(X3, y3)
r2_3 = r2_score(y3, model3.predict(X3))

axes[1, 0].scatter(X3, y3, alpha=0.5, color='orange')
axes[1, 0].plot(sorted(X3), model3.predict(np.array(sorted(X3)).reshape(-1,1)), color='red', linewidth=2)
axes[1, 0].set_xlabel('Price ($)')
axes[1, 0].set_ylabel('Total Sales ($)')
axes[1, 0].set_title(f'Price vs Total Sales\nR2 = {r2_3:.4f}', fontweight='bold')

# Quantity vs Total_Sales
X4 = sales_df[['Quantity']].values
model4 = LinearRegression().fit(X4, y3)
r2_4 = r2_score(y3, model4.predict(X4))

axes[1, 1].scatter(X4, y3, alpha=0.5, color='teal')
axes[1, 1].plot(sorted(X4), model4.predict(np.array(sorted(X4)).reshape(-1,1)), color='red', linewidth=2)
axes[1, 1].set_xlabel('Quantity')
axes[1, 1].set_ylabel('Total Sales ($)')
axes[1, 1].set_title(f'Quantity vs Total Sales\nR2 = {r2_4:.4f}', fontweight='bold')

plt.tight_layout()
plt.savefig('regression_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print('Created: regression_analysis.png')

print('\nAll visualizations created successfully!')
