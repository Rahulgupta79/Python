class NegativeAgeError(Exception):
    def __init__(self):
        print("Age can't be negative")
try:
    age=int(input("Enter your age="))
    if(age<0):
        raise NegativeAgeError
    elif(age>=18):
        print("You are elisible for vote")
    else:
        print("Your age is =",age)
except NegativeAgeError as obj:
    print(obj)
    # print(obj.__class__)