# import numpy as np
# n=int(input("Enter size of array="))
# lst=[]
# for i in range(0,n):
#     lst.append(int(input("Enter data:")))

# arr=np.array(lst)
# print(arr)
# print(arr[3])



from numpy import random
print(random.randint(0,12)) #it gives you a integer value from 0 to 12
print(random.rand(2)) #it gives you a float value from 0 to 2
print(random.randint(15, size=(5))) # it gives you random number in form of numpy-array which size 5
print(random.randint(100, size=(3, 5))) #it gives you random number in 2nd dimension
print(random.choice([3, 5, 7, 9])) #it gives you a number from your array choice

# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().
