# ==========================================
# DAY 21 — OOP MINI PROJECT
# LIBRARY MANAGEMENT SYSTEM
# ==========================================

class Book:

    library_name = "AI Engineering Library"

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def display_book(self):
        status = "Available" if self.available else "Issued"
        print(f"\nTitle  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"\n'{self.title}' has been issued.")
        else:
            print(f"\n'{self.title}' is already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\n'{self.title}' has been returned.")
        else:
            print(f"\n'{self.title}' is already available.")

    @classmethod
    def show_library(cls):
        print(f"\nLibrary : {cls.library_name}")

    @staticmethod
    def welcome():
        print("===== LIBRARY MANAGEMENT SYSTEM =====")


class EBook(Book):

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_book(self):
        super().display_book()
        print(f"File Size : {self.file_size} MB")


Book.welcome()
Book.show_library()

book1 = Book("Python Basics", "Guido van Rossum")
ebook1 = EBook("Agentic AI", "OpenAI", 12)

book1.display_book()
book1.issue_book()
book1.display_book()

ebook1.display_book()

print("\n===== isinstance() =====")
print(isinstance(book1, Book))
print(isinstance(ebook1, EBook))
print(isinstance(ebook1, Book))
