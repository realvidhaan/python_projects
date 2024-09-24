class Dog:
  def __init__(self, name, age ):
    self.name = name
    self.age = age 
  #making some variables to use later
  def bark(self):
    return f"{self.name} says bark"
  #what to do when mypet.bark() is called
collar = input("What is your dog's name ")
#asking user for what the name of the dog will be
year = input(f"What is {collar}'s age ")
#asking the user for what the dog's age should be
mypet = Dog(collar, year)
#making a variable that has the class dog, and the dog class stores the variables collar(name), and year(age).
print(mypet.bark())
#this calls the definition bark, and then getting the print statement from it. Then the print statement executes with the variable for name
print(mypet.age)
#this gets the variable age that the user creates, and then it prints the age of the dog.