class Employee:

    def __init__(self,no,name,domain,position,salary):
        self.no=no
        self.name=name
        self.domain=domain
        self.position=position
        self.salary=salary
    def __str__(self):
        return self.name

f=open("employee file","r")
emplst=[]
for lines in f:
    no,name,domain,position,salary=lines.rstrip("\n").split(",")
    emplst.append(Employee(no,name,domain,position,salary))

developers=list(filter(lambda emp:emp.domain=="developer",emplst))
for emp in developers:
    print(emp.name)
