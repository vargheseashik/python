arr=[10,11,12,14,15]
flag=0
num=int(input("enter the number to be inserted"))
for i in arr:
    if(i==num):
         flag=1
    else:
        flag=0
if(flag==1):
    print("element found")
else:
    print("element not found")
