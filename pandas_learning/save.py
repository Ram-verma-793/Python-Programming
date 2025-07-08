import pandas as pd
data = {
    "name" : ['ram', 'avi', 'ani'],
    "age" : [20, 15, 20],
    "city" : ['smpr', 'jaipur', 'smpr']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("students.csv", index=False) # saving to csv file
df.to_excel("students2.xlsx", index=False)
