class evr(Exception):
    def __init__(self):
        print("Five se Division nhi kiya jata hai")

a=int(input("Enter a number="))
b=int(input("Enter a number="))
try:
    if(b==5):
        raise evr
    else:
        m=a/b
except evr as obj:
    print(obj.__class__)
    print(obj)
else:
    print(m)
finally:
    print("Hello")