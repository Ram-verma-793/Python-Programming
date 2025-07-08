import pandas as pd

data = {
    'name' : ["ram", "shyam", "avi", "anil", "ani"],
    'age'  : [20, 35, 15, 25, 20],
    'salary' : [50000, 20000, 35000, 50000, 55000]

}
df = pd.DataFrame(data)
print(df)
print("shape:\n", df.shape)
print("columns:\n", df.columns)