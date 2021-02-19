class Student:
    cname="cms"


    def __init__(self,roln,name):
        self.rollno = roln
        self.name = name


    def print_values(self):
        print(self.rollno)
        print(self.name)
        print(Student.cname)

ob=Student(100,"ajay")
ob.print_values()