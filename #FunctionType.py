# Function-It is a block of code which is reusable it is so fast to-
#       execute but it has a quality that it perform any work when we call it.
# Every function work or perform his work when it is called
# Function are two types--1.Pre-define/Built In   2.User Define
# Every Function have arguments or parameters and some return value


def add():
    a=int(input("Enter first number="))
    b=int(input("Enter first number="))
    c=a+b
    print("Add=",c)
#No argument without return
def add():
    a=int(input("Enter first number="))
    b=int(input("Enter first number="))
    c=a+b
    return c
#No argument with return
def add(a,b):
    c=a+b
    print("Add=",c)
#with argument No return
def add(a,b):
    c=a+b
    return c
#with argument with return

# Default Parameter-it is new approach which tells that arguments which we pass its depends on us and
#  in this type of some function parameters are define directly to function and our function work perfectly
def default(a,b,c=10):
    d=a+b+c
    print(d)
#  if we create a function which have 3 parameters and we pass 2 arguments then 3rd argument-
#  we can also pass in function 
default(4,5)
#  if we pass total arguments then default parameters are forgeted by function full priority to argumnets
default(4,5,7)