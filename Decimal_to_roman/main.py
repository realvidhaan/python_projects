user_input = int(input("NUMBER: ")) # asking user for input
roman = {
    1000: 'M',
    900: 'CM',
    800: 'DCCC',
    700: 'DCC',
    600: 'DC',
    500: 'D',
    400: 'CD',
    300: 'CCC',
    200: 'CC',
    100: 'C',
    90: 'XC',
    80: 'LXXX',
    70: 'LXX',
    60: 'LX',
    50: 'L',
    40: 'XL',
    30: 'XXX',
    20: 'XX',
    19: 'XIX',
    18: 'XVIII',
    17: 'XVII',
    16: 'XVI',
    15: 'XV',
    14: 'XIV',
    13: 'XIII',
    12: 'XII',
    11: 'XI',
    10: 'X',
    9: 'IX',
    8: 'VIII',
    7: 'VII',
    6: 'VI',
    5: 'V',
    4: 'IV',
    3: 'III',
    2: 'II',
    1: 'I'} # making a dictionary called roman that has the roman numeral keys

roman_numeral = '' # making empty quotes to add to later
if user_input == 0: # making a conditional saying if user equal to 0...
  print("NUMERAL: 0") # ...print the roman numeral is 0
if user_input in roman: # making a conditional saying if user in the roman dictionary...
  final = roman[user_input] #...make a variable final that is equal to which number in roman numerals that the user typed
  print(f"NUMERAL: {final}") # print the roman numeral is the final variable
elif user_input not in roman: # else if user not in the dict roman
  for number, symbol in roman.items(): # make a for loop saying the first key (number) and the second key (symbol) in the items of the roman dict 
    while user_input >= number: # make a while loop saying while user is greater than or equal to number
      roman_numeral += symbol # roman numeral plus symbol
      user_input -= number # and user minus the number

print(f"NUMERAL: {roman_numeral}") # print what the roman numeral is