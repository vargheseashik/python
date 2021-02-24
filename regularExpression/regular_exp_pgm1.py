import re

pattern="ab"

matcher=re.finditer(patterna,"ababababbbbbaabaab")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)