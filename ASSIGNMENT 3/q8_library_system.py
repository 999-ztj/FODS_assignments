"""
This program is a basic Library Management System.
It allows users to: borrow a book, return a book, and search for a book.
It uses OOP (classes), file handling for storing book data, and try/except
for exception handling.
"""

import csv
import os

BOOKS_FILE = "books.csv"


class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        # is_available: True means book is in the library
        self.is_available = is_available


class Library:
    def __init__(self):
        # Load books from file when library starts
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            if not os.path.exists(BOOKS_FILE):
                # Create default books file if it doesn't exist
                self.create_default_books()

            file = open(BOOKS_FILE, "r")
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                if len(row) == 4:
                    available = row[3] == "True"
                    books.append(Book(row[0], row[1], row[2], available))
            file.close()

        except Exception as e:
            print("Error loading books:", e)

        return books

    def create_default_books(self):
        try:
            file = open(BOOKS_FILE, "w", newline="")
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "is_available"])
            writer.writerow(["B001", "Introduction to Python", "John Smith", "True"])
            writer.writerow(["B002", "Data Science Basics", "Surav joshi", "True"])
            writer.writerow(["B003", "Machine Learning", "Jenith Gurung", "True"])
            writer.writerow(["B004", "Database Systems", "Sara kc", "True"])
            file.close()
        except Exception as e:
            print("Error creating books file:", e)

    def save_books(self):
        try:
            file = open(BOOKS_FILE, "w", newline="")
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "is_available"])
            for book in self.books:
                writer.writerow([book.book_id, book.title, book.author, book.is_available])
            file.close()
        except Exception as e:
            print("Error saving books:", e)

    def search_book(self, search_term):
        print()
        print(f"Search results for '{search_term}':")
        print("-" * 50)
        found = False
        for book in self.books:
            # Search in title or author (case-insensitive)
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                status = "Available" if book.is_available else "Borrowed"
                print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | {status}")
                found = True
        if not found:
            print("No books found.")

    def borrow_book(self, book_id):
        try:
            for book in self.books:
                if book.book_id == book_id:
                    if book.is_available:
                        book.is_available = False
                        self.save_books()
                        print(f"You have borrowed '{book.title}'. Please return it on time.")
                    else:
                        print(f"Sorry, '{book.title}' is already borrowed.")
                    return
            print(f"Book with ID '{book_id}' not found.")

        except Exception as e:
            print("Error borrowing book:", e)

    def return_book(self, book_id):
        try:
            for book in self.books:
                if book.book_id == book_id:
                    if not book.is_available:
                        book.is_available = True
                        self.save_books()
                        print(f"Thank you for returning '{book.title}'.")
                    else:
                        print(f"'{book.title}' was not borrowed.")
                    return
            print(f"Book with ID '{book_id}' not found.")

        except Exception as e:
            print("Error returning book:", e)

    def display_all_books(self):
        print()
        print("=== All Books ===")
        print("-" * 60)
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"ID: {book.book_id} | {book.title} | {book.author} | {status}")
        print("-" * 60)


# Main program
library = Library()

print("=== Library Management System ===")
print()

while True:
    print("1. Search for a Book")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View All Books")
    print("5. Exit")
    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        keyword = input("Enter book title or author to search: ")
        library.search_book(keyword)
        print()

    elif choice == "2":
        library.display_all_books()
        book_id = input("Enter Book ID to borrow: ")
        library.borrow_book(book_id)
        print()

    elif choice == "3":
        library.display_all_books()
        book_id = input("Enter Book ID to return: ")
        library.return_book(book_id)
        print()

    elif choice == "4":
        library.display_all_books()
        print()

    elif choice == "5":
        print("Thank you for using the Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        print()
