import pandas as pd

# read from excel file
excel_file = pd.read_excel("students2.xlsx")
print("Excel file reading: \n", excel_file)

# reading specific columns
# excel_file = pd.read_excel("students2.xlsx", usecols=["name", "age"]) # it will prints only name and age data
# we can also read columns by index
excel_file = pd.read_excel("students2.xlsx", usecols=[0, 1])
print("Excel file reading: \n", excel_file)
# print all column names first
print(excel_file.columns)

# we can also filter rows too
filtered_row1 = excel_file[excel_file["age"] > 10]
print("filtered row by as: ", filtered_row1)