import imports_module.MathModule

num1=int(input("enter the Ist number"))
num2=int(input("enter the 2nd number"))

Data1=imports_module.MathModule.add(num1,num2)
print("sum is ",Data1)

Data2=imports_module.MathModule.sub(num1,num2)
print("Substraction is ",Data2)

Data3=imports_module.MathModule.div(num1,num2)
print("Division is ",Data3)

Data4=imports_module.MathModule.mul(num1,num2)
print("Multiplication is ",Data4)

Data5=imports_module.MathModule.mod(num1,num2)
print("Modulus is ",Data5)