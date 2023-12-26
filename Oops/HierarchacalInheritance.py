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

s1=son1()
s1.showSon1()
s1.show()
s2=son2()
s2.showSon2()
s2.show()