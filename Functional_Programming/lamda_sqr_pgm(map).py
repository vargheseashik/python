lst=[2,4,5,6,7]
square=list(map(lambda num:num**2,lst))
print(square)

names=["ajay","ram","sam"]
uc=list(map(lambda name:name.upper(),names))
print(uc)

numbers=[4,5,8,9,3,2]
lst=list(map(lambda num:num+1 if num>5 else num-1,numbers))
print(lst)

marks=[40,45,20,28,30]
marklst=list(map(lambda mark:"fail" if mark<35 else "pass",marks))
print(marklst)