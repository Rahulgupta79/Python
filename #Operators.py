# Operator=Operators are those who performs some specific operation. Python has a wide variety of operators.
#             The various Python operators are categorized into:
#     1-Arithmetic  ( + , - , * , / , % , ** , //) it is use in numbers
#     2-Relational  ( > , >= , < , <= , == , !=) it is use in numbers
#     3-Assignment  ( = ,+= ,-= ,*= , /= , %=) it is use in numbers
#     4-Logical     ( and , or , not)  it is use in numbers
#     5-Identity    ( is , is not) it is use in numbers and also variables
#     6-Membership  ( in , not in) it is use to check value existance in list,tuple,etc
#     7-Bitwise     ( & , | , ^ , ~ , << , >>) it is use in binary numbers

# Arithmetic operators-:
print("\nArithmetic operators-:")
a=5
b=6
print("Addition=",a+b)
print("Substraction=",a-b)
print("Multiplication=",a*b)
print("Division=",a/b)
print("Modulus=",a%b)
print("Exponent=",a**b)
print("Floor Division=",a//b)

#  Relational operators-:
print("\nRelational operators-:")
print("Greater than",a>b)
print("Greater than Equal to",a>=b)
print("Less than",a<b)
print("Less than Equal to",a<=b)
print("Equal to",a==b)
print("Not Equal to",a!=b)
# Assignment operators-:
print("\nAssignment operators-:")
c=a+b
print("Assign Value=",c)
c+=a
print("Add & Assign=",c)
c-=a
print("Substract & Assign=",c)
c*=a
print("Multiply & Assign=",c)
c/=a
print("divide & Assign=",c)
c%=a
print("Modulus & Assign=",c)

# Logical operators-:
print("\nLogical operators-:")
x=3
y=4
z=5
print("Logical and = ",(x<y)and(y<z))
print("Logical or = ",(x<y)or(y<z))
print("Logical not = ",not(y<z))

# Identity operators-: this operator is use to check value of variable is same or not and  same type or not
print("\nIdentity operators-:")
l=3
m=3
print(" is operator(same)=",l is m)
print("is not operator(not same)=",l is not m)
print("variable type",type(l)is int)

# Membrship operators-:
print(" Membrship operators-:")
a=[1,2,3,4,5]  #it is list to check value of l is exist or not in a list
print("in operator =",l in a)
print(" not in operator =",l not in a)

# Bitwise operators-:
j=3
k=4
print(" Bitwise operators-:")
print("Bitwise and operator=",j&k)
print("Bitwise or operator=",j|k)
print("Bitwise XOR operator=",j^k)
print("Bitwise Complement operator=",~j)
print("Bitwise left shift operator=",j<<1)
print("Bitwise right shift operator=",j>>1)
# 0011=3
# 0110=6
# 0010=10=2 Ans

# 00000011=3
# 00000100=4
# 00000000=0 Ans