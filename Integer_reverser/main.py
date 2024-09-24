def int_reverser():
  while True:
      try:
          num = int(input("positive number: "))  # Get input from user and convert to integer
          break  # Exit the loop if the input is valid
      except ValueError:
          print("Please enter a valid integer." )  # Print a more helpful error message

  reverse = 0  # Initialize reverse variable to 0

  while num > 0:  # Continue loop until num is greater than 0
      reverse = reverse * 10  # Shift digits of reverse left by one place
      reverse = reverse + (num % 10)  # Add the last digit of num to reverse
      num = num // 10  # Remove the last digit from num by integer division

  print(reverse)  # Print the reversed number

# Call the function
int_reverser()
