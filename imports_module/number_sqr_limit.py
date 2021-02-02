import math
inc=int(input("enter the number"))

ll=int(input("enter the upper limit"))
ul=int(input("enter the lower limit"))

for i in range(1,ul+1):
    num=math.pow(i,inc)
    if(num>ll)and(num<ul):
        print(num,"is",i,inc)