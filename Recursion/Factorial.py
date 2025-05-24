#Q. Write a Program to Calculate Factorial of a Number Using Recursion

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

n = int(input("Enter N: "))
print("Factorial:", factorial(n))
