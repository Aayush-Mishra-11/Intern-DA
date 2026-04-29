# Setup & Load Data - Install pandas, create file, load CSV
print("Setup & Load Data - Install pandas, create file, load CSV")
import pandas as pd
df = pd.read_csv('sales_data.csv')
print(df)

#--------------------------------------------------------------------
# Explore Data - Check shape, columns, data types
print("\nExplore Data - Check shape, columns, data types")
print(f"\nNumber of rows: {len(df)}") # for the number of rows in the dataset
print(f"Number of columns: {len(df.columns)}") # for the number of columns in the dataset
print(f"\nColumn names: {list(df.columns)}") # column names in the dataset

print("\nData Types:")
print(df.dtypes) # for the data types of each column
1
print("\nshape:")
print(df.shape) # for the shape of the data

print("\nDataset Info:")
print(df.info())# foe Dataset Info

print("\nSummary Statistics:")
print(df.describe()) # for summary statistics of numeric columns

#--------------------------------------------------------------------
# Clean Data - Handle missing values, remove duplicates
print("\nClean Data - Handle missing values, remove duplicates")
print(df.isnull().sum()) # for missing values in each column
df.dropna(inplace=True) # Remove rows with missing values
df.drop_duplicates(inplace=True) # Remove duplicate rows

#--------------------------------------------------------------------
# Analyze Sales - Calculate revenue, find best product
print("\nAnalyze Sales - Calculate revenue, find best product") 
df['Revenue'] = df['Quantity'] * df['Price']
revenue_by_product = df.groupby('Product')['Revenue'].sum()
print(revenue_by_product)

best_selling_product = revenue_by_product.idxmax()
print(f"Best-selling product: {best_selling_product}")
