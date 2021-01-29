limit1=int(input("enter the limit1"))

limit2=int(input("enter the limit2"))

for i in range(limit1,limit2+1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

