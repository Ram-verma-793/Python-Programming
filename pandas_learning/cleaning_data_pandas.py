import pandas as pd

'''
Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

'''


# empty cells

df = pd.read_csv("students.csv")
new_df = df.dropna()
print("This is the old df: \n", df.to_string())
print("This is the new df with no empty set: \n", new_df.to_string())

# finding the missing data

print("Missing values: \n", df.isnull())


# isnull().sum() == gives the total count of missing values column wise

print("Missing values per column:\n", df.isnull().sum())

# fillna() == this will fill missing values with the specified values
df.fillna({'age' : 20}, inplace=True)
print("after filling data:\n", df)