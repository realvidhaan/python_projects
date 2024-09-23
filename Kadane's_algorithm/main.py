def kadane():
  arr = [-2, -5, 4, 8, -6]
  current = arr[0]
  best = arr[0]
  for i in range(1,len(arr)):
    current = max(arr[i], current + arr[i])
    if current > best:
      best = current
  print(f"The maximum score you can get with the list\n{arr} is {best}")
kadane()