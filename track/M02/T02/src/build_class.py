class Book:
    def __init__(self, title, author, price):
        # Store the received values inside the object
        self.title = title
        self.author = author
        self.price = price

title = input("enter title:").strip()
author = input("enter author:").strip()
price = int(input("enter price:"))

book = Book(title, author, price)

print("BOOK DETAILS")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Price: {book.price}")