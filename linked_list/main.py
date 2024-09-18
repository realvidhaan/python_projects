from linked_lst import LinkedList

def main():
    linked_lst = LinkedList()
    while True:
        print("Welcome to Link List algorithm.")
        print("1. Insert a number in the beginning of the list.")
        print("2. Insert a number in the end of the of the list.")
        print("3. View the entire list.")
        print("4. Exit")
        choice = int(input("What do you want to do, answer in the corresponding numbers? "))

        match choice:
            case 1:
                linked_lst.insert_at_beginning()
            case 2:
                linked_lst.insert_at_rear()
            case 3:
                linked_lst.print_list()
            case 4:
                leave()
                
def leave():
    exit("leaving the program.")
    
if __name__ == "__main__":
    main()