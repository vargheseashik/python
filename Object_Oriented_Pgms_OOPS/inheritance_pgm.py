class Parent:
    def phone(self):
        print("phone method")

class Child(Parent):
    pass


ob=Child()
ob.phone()
print(ob)