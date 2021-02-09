lst=[[10,20,30],[40,50,60],[70,80,90]]
new=[]
for i in range(0,len(lst)):
    for j in lst[i]:
        new.append(j)
print(new)
