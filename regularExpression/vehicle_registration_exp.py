import re

rule="[K][L][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9]"

vehregno=input("enter reg no:")

matcher=re.fullmatch(rule,vehregno)
if matcher==None:
    print("invalid number")
else:
    print("valid number")