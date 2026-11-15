class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Book Title:", self.title)
        print("Book Author:", self.author)


# Create three book objects
book1 = Book("css", "Raza")
book2 = Book("Java Programming", "Ahmad")
book3 = Book("computer science", "Ayesha")

# Display book details
book1.display_info()
print()

book2.display_info()
print()

book3.display_info()