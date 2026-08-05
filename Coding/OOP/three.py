class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} has {self.pages} pages"
    
bk1 = Book("Python 3", 365)
bk2 = Book("C++ 26", 665)
bk3 = Book("Java 26", 565)
bk4 = Book("Ruby", 465)
bk5 = Book("Go", 300)
print(bk1)
print(bk2)
print(bk3)
print(bk4)
print(bk5)


        