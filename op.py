# Inheritance->Single/Multi Level /Multiple
# class abc:
#     a=10 #public variable
#     _b=20 #protected variable
#     ___c=30 #private variable
#     def __init__(self): #Constructor
#         print("Welcome")
#         print(self.___c)

#     def show(self):
#         print("Welcome To")

# class ab(abc):#Single Inheritance
#     def tp(self):
#         print("Other function")

# class demo:
#     pass

# class bc(ab):#Multi Level Inheritance
#     def tpp(self):
#         print("bc Class")
# ob=bc()
# print(ob.a)
# print(ob._b)
# ob.show()
# ob.tp()
# ob.tpp()


# # Single comment
# '''
# Multiple Comment
# Inheritance->Single/Multi Level /Multiple/Hybrid
# Polymorphism
# Abstraction
# Encapsulation
# '''

# Encapsulation
class demo:
    __pwd="A" #private variable
    def __init__(self,n): #Constructor
        self.n=n
        self.__pwd="abc"
        print(self.__pwd)
        print(self.n)

    def show(self,nme):
        self.p=nme
        print(self.p)

obj=demo(5)
obj.show(45)

