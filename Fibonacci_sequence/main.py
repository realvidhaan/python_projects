def fibonacci(n):
  if n == 0 or n == 1:
    return n
  return fibonacci(n-1) + fibonacci(n - 2)

n = 3
print(f"The {n} fibonacci number is {fibonacci(n)}")