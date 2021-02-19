students={
    1000:{"id":1000,"name":"ashik","course":"django","qualification":"mca"},
    1001:{"id": 1001,"name":"akhil","course":"django","qualification":"btech"}

}




def get_students(**kwargs):
    id=kwargs["id"]
    property = kwargs["property"]

    if id in students:
        print(students[id]["name"])
        if property in students[id]:
            print(students[id][property])
    else:
        print("student does not exist")
id=int(input("enter the id"))
property=input("enter the property")
get_students(id=id,property=property)


