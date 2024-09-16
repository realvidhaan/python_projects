from catalog import BookCatalog
from borrow_return import BorrowReturn

def main():
    catalog = BookCatalog('data_files/books.json')  
    borrow_return = BorrowReturn('data_files/books.json')
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View all books in the catalog")
        print("4. Find a specific book")
        print("5. Check availability of a book")
        print("6. Check overdue books")
        print("7. Add a book to the catalog")
        print("8. Remove a book from the catalog")
        print("9. Update a book's information")
        print("10. Exit")
        
        choice = input("Please select an action by entering the corresponding number: ")
        
        match choice:
            case "1":
                borrow_return.borrow_book()
            case "2":
                borrow_return.return_book()
            case "3":
                catalog.list_book()
            case "4":
                catalog.find_book()
            case "5":
                catalog.check_availability()
            case "6":
                borrow_return.check_overdue_books()
            case "7":
                catalog.add_book()
            case "8":
                catalog.remove_book()
            case "9":
                catalog.update_book()
            case "10":
                leave()
            case _:
                print("Invalid input. Please try again.")

def leave():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main()
