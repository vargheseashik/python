lst=[1,2,3,4]
inp=int(input("enter the number"))
low=0
upp=len(lst)-1
for i in range(0,len(lst)):
    sums=lst[low]+lst[upp]
    if(sums==inp):
        print("pairs",lst[low],lst[upp])
        break
    elif(sums<inp):
        low+=1
    else:
        upp-=1