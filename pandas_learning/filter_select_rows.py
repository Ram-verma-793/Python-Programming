import pandas as pd

data = {
    'name' : ["ram", "shyam", "avi", "anil", "ani"],
    'age'  : [20, 35, 15, 25, 20],
    'salary' : [50000, 20000, 35000, 50000, 55000]

}
df = pd.DataFrame(data)
print(df)

# single row 
high_age = df[df["age"] > 25]
print("Above age of 25:\n", high_age)

# multiple rows
high_age_with_high_salary = df[(df['age'] > 20) & (df['salary'] > 35000)]
print("high age with high salary:\n", high_age_with_high_salary)

# we can use or operator instead of and to filter more