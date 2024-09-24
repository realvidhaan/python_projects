def reverse(p):
 return p[::-1]

inputStr = str(input("Word: "))

  
reverseStr = reverse(inputStr)
if len(inputStr) == 1:
  print("Please put in a full word")
  exit()
if inputStr == reverseStr :
  print(f"{inputStr} is a palindrome")
else:
  print(f"{inputStr} is not a palindrome")

print(f"The reverse of {inputStr} is {reverse(inputStr)}")