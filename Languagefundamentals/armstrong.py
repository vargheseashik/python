num=int(input("enter number"))
sum=0
while(num>0):
    rem=num%10
    cube=rem*rem*rem+sum
    sum=cube
    num=num//10
print(sum)