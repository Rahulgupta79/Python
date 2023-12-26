class father:
    surname="Gupta"
    def show(self):
        print(self.surname)
class son1(father):
    def showSon1(self):
        print("Son1 ",end="")
class son2(father):
    def showSon2(self):
        print("Son2 ",end="")
class demo(son1,son2):
    def showSon3(self):
        print("This is demo class!")
s1=demo()
s1.showSon3()
s1.showSon1()
s1.show()
s1.showSon2()
s1.show()