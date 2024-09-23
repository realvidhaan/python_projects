def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


def binary_search(arr, n):
  print(arr)
  left = 0
  right = len(arr) - 1

  while left <= right:

    mid = left + (right - left) // 2
    print(f"l:{left} m: {mid} r:{right}")
    if n == arr[mid]:
      print("Found")
      return
    elif n < arr[mid]:
      right = mid - 1
    else:
      left = mid + 1
  print("Not found")


arr = [23, 4, 43, 78, 12, 22, 45, 88, 2, 17]
arr = bubble_sort(arr)
binary_search(arr, 45)
