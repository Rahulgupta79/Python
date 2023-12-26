# Sets are used to store multiple items in a single variable.
# Sets are use curly braces { }
# A set is a collection which is unordered, unchangeable*, and un-indexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered means sets element have not a specified location it may be 2 index another time it will 5 index


t = {"apple", "banana", "cherry"}
print(t)

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can remove or add new items.

th = {"apple", "banana", "cherry"}

for x in th:
  print(x)

th.add(23) #to add a element in set but it add only one element at a time
print(th)

th.remove(23) #to remove a element from set
print(th)

th.discard("apple") # to remove a element from set 
print(th)

print(th.pop()) #to remove a element from set but it show which element will pop
print(th)

th.add("magic")
print(th)
