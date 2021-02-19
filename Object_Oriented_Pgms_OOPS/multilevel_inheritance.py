class Parent:
    def m1(self):
        print("print parent class")

class Child(Parent):
    def m2(self):
        print("print child class")

class Subchild(Child):
    def m3(self):
        print("print subchild class")


object=Subchild()
object.m3()
object.m2()
object.m1()



