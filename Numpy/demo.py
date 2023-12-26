import numpy as np

tp=[] #Blank lIst
n=int(input("Enter size of array:")) #For List size
for i in range(0,n):
    tp.append(int(input("Enter a number:"))) #Insert data in list 

arr=np.array(tp) #list data assign to NumPy Array
# tup=tuple(tp) #list data assign to tuple 
# arr=np.array(tup) #tuple data assign to NumPy Array
# sett=set(tp)
# arr=np.array(sett)

# print(tp) #List
# print(tup) #Tuple
# print(sett) #Set
print(arr) #Array
# print(type(arr))
# print(np.__version__) #It tells NumPy library version

# Array is manipulate by Index in loop
for j in range(0,n):
    print("\t",arr[j])