try:
  vowel_counter = 0
  consonant_counter = 0 
  user = str(input("String: "))
  vowels = ['a', 'e', 'i', 'o','u']
  consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
  for vowel in vowels:
    if vowel in user:
      vowel_counter += 1

  for consonant in consonants:
    if consonant in user:
       consonant_counter +=1
  print(f"There are {consonant_counter} consonant(s) in {user}")
  print(f"There are {vowel_counter} vowel(s) in {user}")
except ValueError:
  print("You can only enter characters that are in the English alphabet.")
