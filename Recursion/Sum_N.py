#Q. Write a Program to Find Sum of N Natural Numbers (entered by users) using Recursion

def sum_n(n):
    return 1 if n == 1 else n + sum_n(n-1)

n = int(input("Enter N: "))
print("Sum:", sum_n(n))
