f=open("demo.py","r")
names=[]
for lines in f:
    names.append(lines.rstrip("\n"))
print(names)