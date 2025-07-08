import pandas as pd

# read data from csv file into a dataframe

df = pd.read_csv(r"Pandas_learning\datasets\Books.csv", encoding="latin1")
# df = pd.read_excel(r"Pandas_learning\datasets\Covid Dashboard.xlsx")
print(df)