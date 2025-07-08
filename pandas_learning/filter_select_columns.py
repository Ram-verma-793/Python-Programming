import pandas as pd

# selecting a specific column
# filter rows
# combine multiple conditions

data = {
    'name' : ["ram", "shyam", "avi", "anil", "ani"],
    'age'  : [20, 35, 15, 25, 20],
    'salary' : [50000, 20000, 35000, 50000, 55000]

}
df = pd.DataFrame(data)
print(df)

column_single = df["name"] # selecting a single column
print("single column:\n", column_single)


column_multiple = df[["name", "salary"]]
print("multiple columns:\n", column_multiple) # to select multiple columns you need to pass them in a list

# filtering rows

filter_single_condition = df[df["salary"] > 35000]
print("single condition filtering:\n", filter_single_condition)

filter_multiple_condition = df[(df["salary"] >35000) & (df["salary"] < 50000)]
print("filtering multiple conditions:\n", filter_multiple_condition)



