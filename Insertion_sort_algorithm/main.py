def insertion_sort(): # defining function
  arr = [88, 9, 5, 3, 80, 78, 70] # making an array
  for i in range(1, len(arr)): # making a for loop, iterating over i for the amount of numbers in the array minus the first integer
    key = arr[i] # making a variable (key) that is the value of i in the array 
    j = i-1  # making a variable j that is the value of the index i but minus one
    while j >= 0 and key < arr[j]: # making a while loop saying when j is equal to or greater than zero, and key is greater than the value of j in the array...
      arr[j+1] = arr[j] # ...the value of j in the array plus one, is equal to the value of j in the array
      j-=1 # making the index of j minus one 
    arr[j+1] = key # making the value of j in the array plus one is equal to key
  print(arr) # showing on the screen the new, sorted array
insertion_sort() # calling the function insertion_sort so the code can actually run