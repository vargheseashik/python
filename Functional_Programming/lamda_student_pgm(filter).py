class Student:
    def __init__(self,roll,name,course,mark):
        self.rollno=roll
        self.name=name
        self.course=course
        self.mark=mark
    def __str__(self):
        return self.name

st=Student(100,"ajay","mca",450)
st1=Student(101,"vijay","bca",500)
st2=Student(102,"ram","mca",550)
st3=Student(103,"sam","bca",600)
Students=[]
Students.append(st)
Students.append(st1)
Students.append(st2)
Students.append(st3)


studentmca=list(map(lambda stud:stud.name,list(filter(lambda stud:stud.course=="mca",Students))))
print("students in mca courses are",studentmca)

maxmarks=max(list(map(lambda stud:stud.mark,Students )))
print("maximum marks of students",maxmarks)