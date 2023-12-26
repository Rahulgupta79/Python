import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
n= arr.reshape(4, 3) #it tells row and col define here means 2-dimensional
# n= arr.reshape(2, 3, 2) #It tells about 3-dimensional
print(n)
print(n[1,1])