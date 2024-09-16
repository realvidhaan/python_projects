import json
import datetime
from datetime import timedelta

class BorrowReturn:
    def __init__(self, catalog_file='data_files/books.json'):
        self.catalog_file = catalog_file
        self.load_books()
        
    def load_books(self):
        try:
            with open(self.catalog_file, 'r') as file_one:
                self.books = json.load(file_one)
        except FileNotFoundError:
            self.books = []
            
    def borrow_book(self):
        borrow = input("What is the title of the book you want to borrow? ").strip().lower()
        for book in self.books:
            if borrow == book['title'].strip().lower():
                if book['available']:
                    user = input(f"{book['title']} is available for checkout.\nWhat is your name? ").strip()
                    print(f"{book['title']} is due in 14 days.")
                    borrow_date = datetime.datetime.now()
                    due_date = borrow_date + timedelta(days=14)
                    due_date_str = due_date.strftime("%Y-%m-%d")
                    book['available'] = False
                    book['borrower'] = user
                    book['due'] = due_date_str
                    with open(self.catalog_file, 'w') as file_one:
                        json.dump(self.books, file_one, indent=4)
                    return
                else:
                    print(f"{book['title']} is not available.")
                    return
        print(f"{borrow} was not found.")

    def return_book(self):
        unborrow = input("What is the title of the book you want to return? ").strip().lower()
        for book in self.books:
            if unborrow == book['title'].strip().lower():
                if not book['available']:
                    user = input("What is the person's name that checked out this book? ").strip()
                    if user == book['borrower']:
                        book['available'] = True
                        book['borrower'] = None
                        book['due'] = None
                        print(f"{book['title']} has been successfully returned.")
                        with open(self.catalog_file, 'w') as file_one:
                            json.dump(self.books, file_one, indent=4)
                        return
                    else:
                        print("The name does not match the borrower.")
                        return
                else:
                    print(f"{book['title']} cannot be returned because it is available for checkout.")
                    return
        print(f"{unborrow} was not found.")
        
    def check_overdue_books(self):
        now = datetime.datetime.now()
        overdue_books = []
        for book in self.books:
            if not book['available']:
                due_date = datetime.datetime.strptime(book['due'], "%Y-%m-%d")
                if now > due_date:
                    overdue_books.append(f"{book['title']} (Borrower: {book['borrower']}, Due: {book['due']})")
        if overdue_books:
            print("The following books are overdue:")
            for overdue in overdue_books:
                print(overdue)
        else:
            print("No books are overdue.")
