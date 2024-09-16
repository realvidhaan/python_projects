import json

class BookCatalog:
    def __init__(self, catalog_file='data_files/books.json'):
        self.catalog_file = catalog_file
        self.load_books()

    def load_books(self):
        try:
            with open(self.catalog_file, 'r') as file_one:
                self.books = json.load(file_one)
        except FileNotFoundError:
            self.books = []

    def add_book(self):
        title = input("What is the title of the book? ").strip()
        author = input("What is the author of the book? ").strip()
        genre = input("What is the genre of the book? ").strip()
        book = {"title": title, "author": author, "genre": genre, "available": True, "borrower": None, "due": None}
        self.books.append(book)
        with open(self.catalog_file, 'w') as file_one:
            json.dump(self.books, file_one, indent=4)
        print(f"{title} has been successfully added to the catalog!")

    def list_book(self):
        if not self.books:
            print("No books in the catalog.")
            return
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Available: {book['available']}")

    def find_book(self):
        search = input("Enter the title of the book you are looking for: ").strip().lower()
        for book in self.books:
            if search == book['title'].strip().lower():
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Available: {book['available']}")
                return
        print(f"{search} was not found in the catalog.")

    def check_availability(self):
        search = input("Enter the title of the book to check its availability: ").strip().lower()
        for book in self.books:
            if search == book['title'].strip().lower():
                if book['available']:
                    print(f"{book['title']} is available for borrowing.")
                else:
                    print(f"{book['title']} is currently checked out.")
                return
        print(f"{search} was not found in the catalog.")

    def remove_book(self):
        remove = input("Enter the title of the book you want to remove: ").strip().lower()
        for book in self.books:
            if remove == book['title'].strip().lower():
                self.books.remove(book)
                with open(self.catalog_file, 'w') as file_one:
                    json.dump(self.books, file_one, indent=4)
                print(f"'{remove}' was deleted from the catalog.")
                return
        print(f"{remove} was not found in the catalog.")

    def update_book(self):
        update = input("Enter the title of the book you want to update: ").strip().lower()
        for book in self.books:
            if update == book['title'].strip().lower():
                field = int(input("What would you like to update?\n1. Title\n2. Author\n3. Genre\nEnter the number: "))
                if field == 1:
                    new_title = input("Enter the new title: ").strip()
                    book['title'] = new_title
                elif field == 2:
                    new_author = input("Enter the new author: ").strip()
                    book['author'] = new_author
                elif field == 3:
                    new_genre = input("Enter the new genre: ").strip()
                    book['genre'] = new_genre
                with open(self.catalog_file, 'w') as file_one:
                    json.dump(self.books, file_one, indent=4)
                print(f"Book information has been updated.")
                return
        print(f"{update} was not found in the catalog.")
