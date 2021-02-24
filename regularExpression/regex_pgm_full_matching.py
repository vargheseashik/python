#start with a-k
#second character should be a digit & it divisible by 3
#any of character
import re
rule="[a-k][369][a-zA-Z]*"

var_name=input("enter the variable")

matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid character")
else:
    print("valid character")
