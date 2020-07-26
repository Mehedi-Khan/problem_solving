# Defining Book class
class Book:
    def __init__(self, title, author, price=0):
        self.title = title
        self.author = author
        self.price = price

    # Abstract display method to return title, author, price
    def abstract_display(self):
        print(f"Title: {self.title}", f"Author: {self.author}", f"Price: {self.price}", sep="\n")


# Defining MyBook class
class MyBook(Book):
    def __init__(self, title, author, price=0):
        Book.__init__(self, title, author, price)


t = input()
a = input()
p = input()
b = MyBook(t, a, p)
b.abstract_display()


