from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self):
        try:
            user = int(input("What is the value of the head of the of the linked list? "))
            new_node = Node(user)
            new_node.next = self.head
            self.head = new_node
        except ValueError:
            print("The value of the head can only be an integer.")

    def insert_at_rear(self):
        try:
            current = self.head
            while current.next is not None:
                current = current.next
            user = int(input("What is the value of the rear of the of the linked list? "))
            new_node = Node(user)
            current.next = new_node
        except ValueError:
            print("The value of the rear can only be an integer.")

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data} ")
            current = current.next