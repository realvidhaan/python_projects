import random

guess = random.randint(1,100)
user = 0
while user != guess:
  user = int(input("guess"))
  if user > guess:
   print("to high, guess lower")
  elif user < guess:
   print("to low, guess higher") 
  elif user == guess: 
   print("good job that was the answer") 