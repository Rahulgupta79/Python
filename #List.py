# List-It is a collection of different values or different types of items.
# It is totally different from array because it store different data or different types of items.
# All items or values are seperated from comma(,) and all entity are store in square bracket ([])
# a=[] blank list
# In list data store in continuous location start with 0 index as array
# a=[1,2,4,5,6,7,8] define data 
# a=[0,1,2,3,4,5,6] so we can say a[0]=1 a[5]=7 and so on
# we can evaluate/access  every data by loop with indexing
# a=["Rahul","Gupta",1,7979759998,] we can also store different types data like string,int ,float etc
a=[2,3,4,5,6,7]
b=[12,23,34,45,56,67]
print(a)

for i in range(0,len(a)):
    print(a[i],end="")

print()
for i in a:
    print(a)


a.append("Rahul")# we can add more data after intialize a list
print(a)

a.insert(2,22)# we can also insert data at desired location
print(a)

a.remove(22)# we can also delete data from list and it takes only value which we want to delete
print(a)

a.clear()# we can also clear all data from list
print(a)

m=["ram","shyam","krishna","ram"]
print(m)
x=m.count("ram")#In this list we have a function to find frequency of list element
print("Freaquency of ram=",x)

# In list indexing are two types which is forwarding and backwarding 
# In Forward indexing like 0 1 2 3 4 5 6 7 8 9
# In backward indexing like -1 -2 -3 -4 -5 -6 -7 -8 -9
