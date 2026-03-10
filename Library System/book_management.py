from shelf import *
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True


    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}' successfully.")
        else:
            print(f"'{self.title}' is already borrowed.")


    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned '{self.title}' successfully.")
        else:
            print(f"'{self.title}' was not borrowed.")


    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} ({self.year}) - {status}")

b1 = Book(*book1)
b2 = Book(*book2)
b3 = Book(*book3)
b4 = Book(*book4)
b5 = Book(*book5)
b6 = Book(*book6)
b7 = Book(*book7)
b8 = Book(*book8)
b9 = Book(*book9)
b10 = Book(*book10)
b11 = Book(*book11)
b12 = Book(*book12)
books = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]


