# It is the way of control our statements flow which we have to execute and which not 
# These are two types
# 1-Selection statement-It is use to select a statement based on condition and execute it
# 2-Loop statement-It is use to select a statement based on condition and execute it in multiple times



#      Selection Statement
print("Selection Statement-:")
a=5
b=7
# if statement
if(a<b):
    print(b)
# if else statement
if(a<b):
    print(b)
else:
    print(a)
# if else if statement
if(a<b):
    print(b)
elif(a>b):
    print(a)
else:
    print(b)


#       Loops Statement   
print("Loops Statement-:")
# while loop
while(a<=b):#condition
    print(a)
    a+=1 #increment/Decrement
# for loop
for l in range(a,b+1,1):#start,condition,increment/Decrement
    print(l)