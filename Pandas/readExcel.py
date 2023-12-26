import pandas as pd

data=pd.read_csv("C:\\Users\\rahul\\OneDrive\\Desktop\\abc.csv")

# print(data)#It shows all data 
# print(data['Roll'])#it shows a particular column which we want to show or work on it
# lst=["Name","Roll"]
# print(data[lst])

# print(data.head)# it shows only few data as preview from beginning
# print(data.head(1))#it shows few rows as we want

# print(data.tail) #it shows only few data as preview from last
# print(data.tail(1))#it shows few rows as we want

# print(data.shape)#It tells your rows and columns to know quantity of data items

# print(data.info())#it tells of column names and count of rows 

# print(data.describe())#it works on integeric column and give some specific info about data

# print(data.iloc[0])#It shows a particular row by indexing
# print(data.iloc[0:2])#It shows 0 index se 1 index tk ka all data
# print(data.iloc[0,2])#it shows 0 index ka 2 column ka data
