person={"id":100,"name":"ajay","gender":"male"}

print(person["name"])

if "total" in person:
    print("exist")
else:
    person["total"]=150
print(person)


person["total"]+=50
print(person["total"])
print(person)

for i in person:
    print(person[i])