class A:
    def show(self):
        print("Class A")


class B():
    def show1(self):
        print("Class B")

class C(A,B):
    def show2(self):
        print("Class C")

obj=C()
obj.show()
obj.show1()
obj.show2()