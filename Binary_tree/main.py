import random 
import sys 
from typing import Optional 


class Node: 

  def __init__(self, value=None): 
    self.left: Optional[Node] = None
    self.right: Optional[Node] = None
    if value is None:
      value = random.randint(1, 10)
    self.value = value

class BinaryTree:

  def __init__(self):
    self.root = None

  def insert_number(self):
    value = int(input("What number do you want to insert? "))
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return
    current = self.root
    while True:
      if value < current.value:
        if current.left is None:
          current.left = new_node
          break
        else:
          current = current.left
      else:
        if current.right is None:
          current.right = new_node
          break
        else:
          current = current.right

  def search_number(self, num, node):
    if node is None:
      print(f"{num} was not found.")
      return
    if node.value == num:
      print(f"{num} was found.")
      return

    if node.value > num:
      self.search_number(num, node.left)
    elif node.value < num:
      self.search_number(num, node.right)

  def display_tree(self, node):
    if node is not None:
      self.display_tree(node.left)
      print(node.value, end=' ')
      self.display_tree(node.right)

  def delete_number(self, numo, node):
    if node is None:
      print(f"{numo} was not found.")
      return None
      
    if node.value > numo:
      node.left = self.delete_number(numo, node.left)
    elif node.value < numo:
      node.right = self.delete_number(numo, node.right)
    else:
      if node.left is None:
        temp = node.right
        print(f"{numo} has been deleted.")
        return temp
      elif node.right is None:
        temp = node.left
        print(f"{numo} has been deleted.")
        return temp
      temp = self.min_node(node.right)
      node.value = temp.value
      node.right = self.delete_number(node.value, node.right)
    return node

  def min_node(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def exit_code(self):
    sys.exit("Exiting the program. Goodbye!")

  def main(self):
    try:
      while True:
        user = int(
            input(
                "Welcome to the Binary Tree Manager! What would you like to do?\n1. Insert a number\n2. Search for a number\n3. Display the tree (inorder traversal)\n4. Delete a number\n5. Exit\n"
            ))

        match user:
          case 1:
            self.insert_number()
          case 2:
            num = int(input("What number do you want to search for? "))
            self.search_number(num, self.root)
          case 3:
            self.display_tree(self.root)
            print("\n")
          case 4:
            numo = int(input("What number do you want to delete? "))
            self.root = self.delete_number(numo, self.root)
          case 5:
            self.exit_code()
          case _:
            sys.exit("Press the numbers to the corresponding sentences.")
    except ValueError:
      sys.exit("Press the numbers to the corresponding sentences.")


if __name__ == "__main__":
  bt = BinaryTree()
  bt.main()
