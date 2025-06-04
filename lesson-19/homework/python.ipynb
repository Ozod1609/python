import pandas as pd

# Load sales data
sales_df = pd.read_csv("task\\sales_data.csv")

# Add total sale column
sales_df['TotalSale'] = sales_df['Quantity'] * sales_df['Price']

# 1. Group by Category with aggregate statistics
category_stats = sales_df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Max_Quantity_One_Transaction=('Quantity', 'max')
).reset_index()

print("Category Aggregated Stats:\n", category_stats)

# 2. Top-selling product in each category by total quantity sold
top_products = (
    sales_df.groupby(['Category', 'Product'])['Quantity']
    .sum()
    .reset_index()
    .sort_values(['Category', 'Quantity'], ascending=[True, False])
    .groupby('Category')
    .first()
    .reset_index()
)
print("\nTop-selling product in each category:\n", top_products)

# 3. Date with highest total sales
daily_sales = sales_df.groupby('Date')['TotalSale'].sum()
best_sales_day = daily_sales.idxmax()
print(f"\nDate with highest total sales: {best_sales_day} (${daily_sales.max():.2f})")
 Homework Assignment 2: Examining Customer Orders

# Load customer orders
orders_df = pd.read_csv("task\\customer_orders.csv")

# 1. Group by CustomerID and filter customers with >= 20 orders
order_counts = orders_df.groupby('CustomerID').size()
active_customers = order_counts[order_counts >= 20].index
active_customers_df = orders_df[orders_df['CustomerID'].isin(active_customers)]

print("\nCustomers with >= 20 orders:\n", active_customers_df['CustomerID'].unique())

# 2. Customers with avg product price > $120
avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean()
high_price_customers = avg_price_per_customer[avg_price_per_customer > 120].index
print("\nCustomers with average price > $120:\n", high_price_customers.tolist())

# 3. Total quantity and total price per product, filter total quantity < 5
product_stats = orders_df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', 'sum')
).reset_index()

filtered_products = product_stats[product_stats['Total_Quantity'] >= 5]
print("\nProducts with total quantity >= 5:\n", filtered_products)
 Homework Assignment 3: Population Salary Analysis

import sqlite3
import numpy as np
import pandas as pd

# 1. Read from population.db using SQL
conn = sqlite3.connect("task\\population.db")
population_df = pd.read_sql("SELECT * FROM population", conn)

# 2. Read salary bands from Excel
bands_df = pd.read_excel("task\\population salary analysis.xlsx")

# Assume bands_df has 'MinSalary', 'MaxSalary', 'BandName'
# 3. Categorize population into salary bands
def assign_band(salary):
    row = bands_df[(bands_df['MinSalary'] <= salary) & (bands_df['MaxSalary'] >= salary)]
    return row['BandName'].values[0] if not row.empty else 'Unknown'

population_df['SalaryBand'] = population_df['Salary'].apply(assign_band)

# 4. Aggregation by SalaryBand
band_summary = population_df.groupby('SalaryBand')['Salary'].agg(
    PopulationCount='count',
    AverageSalary='mean',
    MedianSalary='median'
).reset_index()

# Add percentage
total_pop = len(population_df)
band_summary['PopulationPercent'] = (band_summary['PopulationCount'] / total_pop) * 100
print("\nOverall Salary Band Summary:\n", band_summary)

# 5. Aggregation by SalaryBand and State
state_band_summary = (
    population_df.groupby(['State', 'SalaryBand'])['Salary']
    .agg(
        PopulationCount='count',
        AverageSalary='mean',
        MedianSalary='median'
    )
    .reset_index()
)

# Add percentage by state
state_totals = population_df.groupby('State')['Salary'].count().rename('StateTotal')
state_band_summary = state_band_summary.merge(state_totals, on='State')
state_band_summary['PopulationPercent'] = (
    state_band_summary['PopulationCount'] / state_band_summary['StateTotal'] * 100
)
state_band_summary.drop(columns=['StateTotal'], inplace=True)

print("\nState-wise Salary Band Summary:\n", state_band_summary)
