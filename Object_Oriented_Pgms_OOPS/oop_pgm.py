class Person:
    def set_values(self,age,name):
        self.age=age
        self.name=name
    def print_values(self):
        print(self.name)
        print(self.age)


object=Person()
object.set_values(25,"ajay")
object.print_values()
