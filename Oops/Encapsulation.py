class Demo:
    __a="" #this is private variable
    def __init__(self):
        print(self.__a)
        self.__a="Magic"
        print(self.__a)

obj=Demo()