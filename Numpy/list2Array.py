import numpy as np

tp=[] #Blank lIst
n=int(input("Enter size of array:")) #For List size
for i in range(0,n):
    tp.append(int(input("Enter a number:"))) #Insert data in list 

print(tp) #List
arr=np.array(tp)
print(arr) #Array