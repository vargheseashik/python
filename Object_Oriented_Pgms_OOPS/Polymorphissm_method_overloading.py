#method overloading
class Maths:
    def add(self):
        print("inside no argument method")
    def add(self,num1):
        print("inside 1 argument method")
    def add(self,num1,num2):
        print("inside 2 argument method")


object=Maths()
object.add(10,20)
object.add(10)
object.add()