class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return str(self.pages)
object=Book(100)
object1=Book(200)
object2=Book(300)
print(object+object1+object2)

