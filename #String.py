# String-It is collection of character which store in contiguous memory location index 
# We know that strings are accessible through loops by using index(forward indexing) 0 1 2 3 4 and so on
# Here we know a new aprroach which is backward indexing like -1 ,-2 ,-3 ,-4 ,-5 and so on
#  0  1  2  3  4  5  ->forward indexing
#  r  o  h  a  n  a
# -6 -5 -4 -3 -2 -1  ->backward indexing
#  String  will also access by character by character and we also use any character index to -
#    work with different programs
#  String is immutable means it can't be updated
str="Sohan"
print(str)

for i in str:
    print(i)

for i in str:
    print(i,end="")

print()

# String Concatination ( + )
str1="Mohan"
print(str+str1)

print()

strp=str+str1
print(strp)

#  String Replication ( * )
ptr="Malhan"
print(3*"Mokam")#in this string integer operator will work to show it multiple times 
print(3*ptr)

#  String Membersgip ( in / not in )
print('h' in ptr)
print('k' not in ptr)

#  String Comparison ( > , < , >= , <= , == , != )
print(str==str1)#String comparison
print('h'=='h')#Character comparison
print('a'=='A')#Character case comparison

# String Slicing-String slicing returns the characters falling between indexes n and m
# Syntax-stringName(start:end:step)
p="Hello World"
print(p[3:9])#in this string characters are printed between index n to m
print(p[6:],p[:6]) #in  this string  characters are printed start and last to 6 index before