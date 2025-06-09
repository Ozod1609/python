mport pandas as pd
import numpy as np

# Create initial DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1. Rename columns using a function
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# 2. Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# 3. Mean age
print("\nMean age:", df['age'].mean())

# 4. Select and print only 'first_name' and 'city' columns
print("\nSelected columns:")
print(df[['first_name', 'city']])

# 5. Add a new column 'salary' with random values
df['salary'] = np.random.randint(40000, 100000, size=len(df))

# 6. Display summary statistics
print("\nSummary statistics:")
print(df.describe(include='all'))
Homework 2: Sales and Expenses Analysis

# Create the DataFrame
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# Calculations
print("\nMaximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

print("\nMinimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())
 3: Monthly Expenses by Category

# Create the DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index
expenses = expenses.set_index('Category')

# Maximum for each category
print("\nMaximum Expense per Category:")
print(expenses.max(axis=1))

# Minimum for each category
print("\nMinimum Expense per Category:")
print(expenses.min(axis=1))

# Average for each category
print("\nAverage Expense per Category:")
print(expenses.mean(axis=1))
