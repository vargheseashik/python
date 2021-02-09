employee=[
    [100,"akhil","developer",2,50000],
    [200, "ram", "tester", 2, 20000],
    [100, "sam", "developer", 2, 80000],
    [100, "arun", "developer", 2, 70000],

]

sum=0

#for emp in employee:
    #print(emp[1])

#for emp in employee:
    #print(emp[4])

#for emp in employee:
    #if emp[2]=="developer":
        #print(emp)

#for emp in employee:
    #sum=sum+(emp[4])
#print(sum)

#sallist=[]
#for emp in employee:
    #sallist.append(emp[4])
#print(max(sallist))

#print employees worked 1990's
#print experieance of each employees
#print high experieance of each employees

exp=[]
for emp in employee:
    exp.append(emp[3]-emp[2])
high=max(exp)
for emp in employee:
    exp=emp[3]-emp[2]
    if(high==exp):
        print(emp)









