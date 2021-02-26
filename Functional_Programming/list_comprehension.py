lst=[1,2,3,4]
op=[num**2 for num in lst]
print("square of numbers",op)

#even numbers
even=[num for num in lst if num%2==0]
print("even numbers",even)

lst=[1,2,3]
lst1=[1,2,3,4]
common=[num for num in lst for num1 in lst1 if num==num1]
print("common numbers in list",common)

lst=[1,2,3]
lst1=[4,5,6]
pair=[(num,num1) for num in lst for num1 in lst1  ]
print("pairs of list",pair)

lst1=[[10,20],[30,40],[50,60]]
list=[num for lst in lst1 for num in lst]
print("non list",list)

lst=[4,3,2,6,7,8,5]
list=[num-1 if num<5  else num+1 if num>5 else 5 for num in lst ]
print(list)