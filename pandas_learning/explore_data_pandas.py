import pandas as pd
# load a csv into a pandas dataFrame
df = pd.read_csv("students.csv")
print(df.to_string())

# creating own dataframe
mydataframe = {
    "Cars" : ["bmw", "mercedes", "tata", "volvo"],
    "Bikes" : ["bmw-850", "RE-gt_650", "lord-splendor", "royal"]
}
my_data = pd.DataFrame(mydataframe)
print(my_data)


# series in pandas
a = [1, 2, 3, 4, 5]
my_series = pd.Series(a)
print("Series in pandas: \n", my_series)


# labels in pandas
b = [12, 15, 256]
my_label = pd.Series(b, index= ["x", "y", "z"])
print("my_label: \n", my_label)

# key-value objects
calories = {
    "day1" : 420,
    "day2" : 450,
    "day3" : 380, 
    "day4" : 760
}
my_calories_data = pd.Series(calories)
print("my calories data: \n", my_calories_data)

# creating and locate row in a dataframe

data = {
    "calories" : [420, 350, 600, 570],
    "days" : [1, 2, 3, 4]
}

df = pd.DataFrame(data)
print("this is my dataframe data: \n", df)
# locating a row 
print("locate: \n", df.loc[[0, 1]]) # it will return the 0 and 1 row data

# give name to indices
data_2 = {
    "calories" : [420, 350, 600, 570],
    "days" : [1, 2, 3, 4]
}
df_2 = pd.DataFrame(data_2, index= ["row1", "row2", "row3", "row4"])
print("named indices: \n", df_2)
# we can locate the indices using their names
print("locating named indices: \n", df_2.loc["row3"])


# load files to a dataframe

df_3 = pd.read_excel("students2.xlsx")
print("This is the excel data that is loaded from a excel file: \n", df_3)



# reading data from a csv file
df_4 = pd.read_csv("students.csv")
print("this is the data from a csv file: \n", df_4)

# we can use .tostring() method to print the entire dataframe
df_5 = pd.read_csv("students.csv")
print("this is the to_string method in the dataframe: \n", df_5)


print("max rows: \n",pd.options.display.max_rows)



# load the json file to dataframe
df_6 = pd.read_json("Pandas_learning\datasets\pokemonDB_dataset.json\pokemonDB_dataset.json")
print("this is the json data: \n", df_6)



# analyzing the dataFrames------------------
# head()  ==  the head() method returns the headers and a specified number of rows, starting from the top

print("THis is the head() method: \n", df_6.head(10))

# tail() == the tail() method is also used for data viewing but the tail method viewing the last rows of the dataframe

print("This is the tail() method: \n", df_6.tail())


# info() == The info() method gives the more information about the data set

print("This is the info() method: \n", df_6.info())