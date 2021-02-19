students={
    1000:{"id":1000,"name":"ashik","course":"django","qualification":"mca"},
    1001:{"id": 1001,"name":"akhil","course":"django","qualification":"btech"}

}

id=int(input("enter student id"))
property=(input("enter student property"))

if id in students:

    if property in students[id]:
        print(students[id][property])
    else:
        print("property unknown")
else:
    print("id unknown")