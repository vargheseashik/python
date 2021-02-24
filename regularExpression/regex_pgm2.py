import re
#character sets
#==============
# pattern='[abc]'
# pattern='[a-z]'
# pattern='[A-Z]'
# pattern='[a-zA-Z]'
#pattern='[0-9]'
# pattern='[a-zA-Z0-9]'
#pattern='[^a-zA-Z0-9^]'#except(^)
#pattern="a+"#check consiqutive a's
#pattern="a*"#any no of a
#pattern="a{2}"#group of 2
#pattern="a{2,3}"#group min 2,max 3

#pre defined characters
#=======================
# pattern="\s"#space
# pattern="\d"digits
# pattern="\D"#except digits
# pattern="\w"#all words
# pattern="\W"#special characters




matcher=re.finditer(pattern,"aaaaaaaaaabaaaabaaaabaa _Z7K@")

for match in matcher:
    print("position of pattern",match.start())
    print("matched at",match.group())
