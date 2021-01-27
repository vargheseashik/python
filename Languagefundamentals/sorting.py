num1 = input("enter num1")
num2 = input("enter num2")
num3 = input("enter num3")

if (num1 >= num2) & (num1 >= num3):
    largest = num1
    if (num2 > num3):
        largest2 = num2
        largest3 = num3
    else:
        largest2 = num3
        largest3 = num2

elif (num2 >= num1) & (num2 >= num3):
    largest = num2
    if (num1 > num3):
        largest2 = num1
        largest3 = num3
    else:
        largest2 = num3
        largest3 = num1

else:
    largest = num3
    if (num1 > num2):
        largest2 = num1
        largest3 = num2
    else:
        largest2 = num2
        largest3 = num1

print("The ascending order is ",largest,"",largest2,"",largest3)
print("The ascending order is ",largest3,"",largest2,"",largest)



