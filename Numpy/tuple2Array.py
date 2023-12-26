import numpy as np

tp=[] #Blank lIst
n=int(input("Enter size of array:")) #For List size
for i in range(0,n):
    tp.append(int(input("Enter a number:"))) #Insert data in list 

print(tp) #List
tup=tuple(tp)
arr=np.array(tup)
print(arr) #Array