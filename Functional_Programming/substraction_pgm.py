# num1=int(input("enter the Ist number"))
# num2=int(input("enter the 2nd number"))
#
# def sub(num1,num2):
#     if num1<num2:
#         (num1,num2)=(num2,num1)
#     return num1-num2
#
# print(sub(num1,num2))


def sub_smart(fun):
    def inner(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return fun(no1,no2)
    return inner



@sub_smart
    return no1-no2
print(sub(10,20))