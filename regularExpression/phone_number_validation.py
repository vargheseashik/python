import re

rule="[0-9]{10}"

phoneno=input("enter mob no:")

matcher=re.fullmatch(rule,phoneno)
if matcher==None:
    print("invalid number")
else:
    print("valid number")