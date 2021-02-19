class Student:
    cname="cms"

    def set_values(self,roln,name):
        self.rollno=roln
        self.name=name
    def print_values(self):
        print(self.rollno)
        print(self.name)
        print(Student.cname)

ob=Student()
ob.set_values(100,"ajay")
#ob.print_values()
print(ob.name)
print(ob.rollno)
print(Student.cname)