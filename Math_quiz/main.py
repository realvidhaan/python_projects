import time

print("Hello, welcome to this math quiz\nYou have one minute to finish the quiz.")

# Wait for 1 second to give users time to read the message
time.sleep(1)

start_time = time.time()
end_time = start_time + 62  # End time is 60 seconds (1 minute) after start time

correct = 0
incorrect = 0
sum = incorrect + correct
while True:
   
    current_time = time.time()
    if current_time >= end_time:
        break  # Exit the loop immediately when time's up

    try:
        bob = int(input("What is 4*10 - 30*5? "))
    except ValueError:
        break  # Exit the loop if the user enters an invalid input

    if bob == 50:
        print("That's correct, good job!")
        correct += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect += 1

    try:
        bobTwo = int(input("What is 7*4 + 80 - 100? "))
    except ValueError:
        break

    if bobTwo == 8:
        print("That's correct, good job!")
        correct += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect += 1

    try:
        bobthree = int(input("What is 4*5*5 - 40 + 13? "))
    except ValueError:
        break

    if bobthree == 73:
        print("That's correct, good job!")
        correct += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect += 1

    try:
        bob4 = int(input("What is 70 / 10 - 5 * 13? "))
    except ValueError:
        break

    if bob4 == 26:
        print("That's correct, good job!")
        correct += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect += 1

    try:
        bob5 = int(input("What is 50 / 2 - 25 * 50000000000000000? "))
    except ValueError:
        break

    if bob5 == 0:
        print("That's correct, good job!")
        correct += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect += 1

    try:
        bob6 = int(input("What is 500 / 10 * 2 / 10? "))
    except ValueError:
        break

    if bob6 == 10:
        print("That's correct, good job!")
        correct += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect += 1

# Display time taken to complete the quiz
elapsed_time = time.time() - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)
print(f"You finished the quiz in {minutes} minutes and {seconds} seconds.")

# Display correct and incorrect answers count
print(f"You got {correct}  out of {sum} correct answers and {incorrect} incorrect answers.")