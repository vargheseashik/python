lst=[4,5,1,3,2,8,9]
lst.sort()
print(lst)
lower=0
upper=len(lst)-1
element=int(input("enter the number to be sorted"))
flag=0


while(lower<=upper):
    mid=(lower+upper)//2

    if element>lst[mid]:
        lower=mid+1

    elif element<lst[mid]:
        upper=mid-1

    elif element==lst[mid]:
         flag=1
         break
if flag==0:
    print("element not found")
else:
    print("element  found")









#print(len(arr))