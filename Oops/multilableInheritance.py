class A:
    def show(self):
        print("Class A")


class B(A):
    def show1(self):
        print("Class B")

class C(B):
    def show2(self):
        print("Class C")

obj=C()
obj.show()
obj.show1()
obj.show2()