class Parent:
    def m1(self):
        print("print parent class")

class Child:
    def m2(self):
        print("print child class")

class Subchild(Parent,Child):
    def m3(self):
        print("print subchild class")


object=Subchild()
object.m3()
object.m1()
object.m2()



