#In Python Tuple are a container where we store set of data in defferent datatype also like list. 
# we cant  manipulate data after insert.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] and so on.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuples data can be of any datatypes like integer,float,string,boolean etc
# Tuples are use small bracket ( )
# In blank tuple or other tuplle you cant insert data if want insert then you first insert data in a list then assign by typeCasting

a=(12,24,76,43,24)
print(a)
print(a.count(24)) #it tells that data which we pass in tuples are how much duplicate
print(a.index(76)) #it tells that data is available or not in tuple and which index
b=("Rahul",32)
print(b)
print(len(a))#It tells tuple length

# th =("apple",)
# print(type(th)) it is a tuple

# NOT a tuple
# th= ("apple")
# print(type(th))it is a string


# List is a collection which is ordered and changeable. Allows duplicate members.

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# Dictionary is a collection which is ordered** and changeable. No duplicate members.

t=()
p=[]
n=int(input("Enter a number="))
for i in range(0,n):
    p.append(int(input("Enter number=")))
print(p)
t=tuple(p)
print(t)