# #method overriding
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return self.name
#
#
# object=Person("ajay",25)
# print(object)


class Student:
    def __init__(self,roll,name,course,mark):
        self.rollno=roll
        self.name=name
        self.course=course
        self.mark=mark

st=Student(100,"ajay","mca",450)
st1=Student(101,"vijay","bca",500)
st2=Student(102,"ram","mca",550)
st3=Student(103,"sam","bca",600)
Students=[]
Students.append(st)
Students.append(st1)
Students.append(st2)
Students.append(st3)
for Student in Students:
    if Student.course=="mca":
        print(Student.name)

marks=[]
for Student in Students:
    marks.append(Student.mark)
    maxx=max(marks)
for Student in Students:
    if Student.mark==maxx:
        print(Student.name)