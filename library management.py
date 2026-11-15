
# Library Management System

# Book Class
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity


# Library Class
class Library:
    def __init__(self):
        self.books = {}
        self.issued_books = []

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                return

        except ValueError:
            print("Please enter a valid number!")
            return

        book = Book(book_id, title, author, quantity)
        self.books[book_id] = book

        print("Book added successfully!")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n----- ALL BOOKS -----")

        for book in self.books.values():
            issued_count = sum(
                1 for item in self.issued_books
                if item["book_id"] == book.book_id
            )

            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Total Quantity:", book.quantity)
            print("Available Quantity:", book.quantity - issued_count)
            print("----------------------")

    # Search Book
    def search_book(self):
        search = input("Enter Book ID or Title: ").strip()

        found = False

        for book in self.books.values():
            if (book.book_id == search or
                    book.title.lower() == search.lower()):

                issued_count = sum(
                    1 for item in self.issued_books
                    if item["book_id"] == book.book_id
                )

                print("\nBook Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available Quantity:",
                      book.quantity - issued_count)

                found = True

        if not found:
            print("Book not found!")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        issued_count = sum(
            1 for item in self.issued_books
            if item["book_id"] == book_id
        )

        available = book.quantity - issued_count

        if available <= 0:
            print("Book is not available!")
            return

        student = input("Enter Student Name: ")

        self.issued_books.append({
            "book_id": book_id,
            "title": book.title,
            "student": student
        })

        print("Book issued successfully!")
        print("Available Quantity:", available - 1)

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID: ")
        student = input("Enter Student Name: ")

        for item in self.issued_books:
            if (item["book_id"] == book_id and
                    item["student"].lower() == student.lower()):

                self.issued_books.remove(item)

                book = self.books[book_id]

                issued_count = sum(
                    1 for record in self.issued_books
                    if record["book_id"] == book_id
                )

                print("Book returned successfully!")
                print("Available Quantity:",
                      book.quantity - issued_count)
                return

        print("No matching issued record found!")

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        for item in self.issued_books:
            if item["book_id"] == book_id:
                print("Cannot delete! Book is currently issued.")
                return

        del self.books[book_id]

        print("Book deleted successfully!")

    # View Issued Books
    def view_issued_books(self):
        if not self.issued_books:
            print("No books are currently issued.")
            return

        print("\n----- ISSUED BOOKS -----")

        for item in self.issued_books:
            print("Book ID:", item["book_id"])
            print("Book Title:", item["title"])
            print("Student Name:", item["student"])
            print("------------------------")


# Main Function
def main():

    library = Library()

    while True:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. View Issued Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.delete_book()

        elif choice == "7":
            library.view_issued_books()

        elif choice == "8":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run Program
if __name__ == "__main__":
    main()

