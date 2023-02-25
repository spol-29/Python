def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
x = input("Enter an integer to find the factorial(!) >>>")
y = int(x)
print("Factorial of int is >>>")
print(factorial(y))