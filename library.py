import tkinter as tk
from tkinter import ttk

class Book:
    def __init__(self, title, author, publication_date, genre, isbn, availability):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.isbn = isbn
        self.availability = availability

class User:
    def __init__(self, name, email, phone_number, borrowed_books):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.borrowed_books = borrowed_books

class Transaction:
    def __init__(self, book_id, user_id, date_borrowed, date_returned):
        self.book_id = book_id
        self.user_id = user_id
        self.date_borrowed = date_borrowed
        self.date_returned = date_returned

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def edit_book(self, book_id, new_title=None, new_author=None, new_availability=None):
        book = self.find_book(book_id)
        if book:
            if new_title:
                book.title = new_title
            if new_author:
                book.author = new_author
            if new_availability:
                book.availability = new_availability
        else:
            print("Book not found.")

    def delete_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            self.books.remove(book)
        else:
            print("Book not found.")

    def borrow_book(self, book_id, user_id):
        book = self.find_book(book_id)
        user = self.find_user(user_id)
        if book and user and book.availability == "available":
            book.availability = "borrowed"
            user.borrowed_books.append(book_id)
            self.transactions.append(Transaction(book_id, user_id, date.today(), None))
        else:
            print("Book not available for borrowing.")

    def return_book(self, book_id, user_id):
        book = self.find_book(book_id)
        user = self.find_user(user_id)
        if book and user and book.availability == "borrowed" and book_id in user.borrowed_books:
            book.availability = "available"
            user.borrowed_books.remove(book_id)
            transaction = self.find_transaction(book_id, user_id)
            transaction.date_returned = date.today()

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    def add_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)

    def delete_user(self, user_id):
        user = self.find_user(user_id)
        if user:
            self.users.remove(user)

lib = Library()
user = User("anem", "sdf@EF", 323232, [])

class LibraryGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")

        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Create frames for each tab
        self.book_tab = ttk.Frame(self.notebook)
        self.user_tab = ttk.Frame(self.notebook)
        self.transaction_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.book_tab, text="Books")
        self.notebook.add(self.user_tab, text="Users")
        self.notebook.add(self.transaction_tab, text="Transactions")

        # Create widgets for the Books tab
        self.books_list = tk.Listbox(self.book_tab, width=80)
        self.books_list.pack(pady=10)

        self.add_book_button = tk.Button(self.book_tab, text="Add Book", command=self.add_book)
        self.add_book_button.pack(side="left", padx=10)

        self.edit_book_button = tk.Button(self.book_tab, text="Edit Book", command=self.edit_book)
        self.edit_book_button.pack(side="left", padx=10)

        self.delete_book_button = tk.Button(self.book_tab, text="Delete Book", command=self.delete_book)
        self.delete_book_button.pack(side="left", padx=10)

        self.withdraw_book_button = tk.Button(self.book_tab, text="Withdraw Book", command=self.withdraw_book)
        self.withdraw_book_button.pack(side="left", padx=10)

        self.return_book_button = tk.Button(self.book_tab, text="Return Book", command=self.return_book)
        self.return_book_button.pack(side="left", padx=10)

        # Create widgets for the Users tab
        self.users_list = tk.Listbox(self.user_tab, width=80)
        self.users_list.pack(pady=10)

        self.add_user_button = tk.Button(self.user_tab, text="Add User", command=self.add_user)
        self.add_user_button.pack(side="left", padx=10)

        self.edit_user_button = tk.Button(self.user_tab, text="Edit User", command=self.edit_user)
        self.edit_user_button.pack(side="left", padx=10)

        self.delete_user_button = tk.Button(self.user_tab, text="Delete User", command=self.delete_user)
        self.delete_user_button.pack(side="left", padx=10)

        # Create widgets for the Transactions tab
        self.transactions_list = tk.Listbox(self.transaction_tab, width=80)
        self.transactions_list.pack(pady=10)

        self.add_transaction_button = tk.Button(self.transaction_tab, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.pack(side="left", padx=10)

        self.delete_transaction_button = tk.Button(self.transaction_tab, text="Delete Transaction", command=self.delete_transaction)
        self.delete_transaction_button.pack(side="left", padx=10)

    def add_book(self):
        # TODO: Implement adding a book
        text = tk.Text(self.books_list)
        text.insert("end", "Hello, World\n")
        text.pack(side="left")
        pass

    def edit_book(self):
        # TODO: Implement editing a book
        pass

    def delete_book(self):
        # TODO: Implement deleting a book
        pass

    def withdraw_book(self):
        # TODO: Implement withdrawing a book
        pass

    def return_book(self):
        # TODO: Implement returning a book
        pass

    def add_user(self):
        # TODO: Implement adding a user
        pass

    def edit_user(self):
        # TODO: Implement editing a
        pass
    def delete_user(self):
        # TODO: Delete a user
        pass
    def add_transaction(self):
        # TODO: Implement add transaction
        pass
    def delete_transaction(self):
        # TODO: Implement delete transaction
        pass

x = LibraryGUI()
x.root.mainloop()
