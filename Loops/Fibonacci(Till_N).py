"""
Q. Write a Program to Display Fibonacci Series upto certain number n (n is entered by user)

Example: n=100
Output:
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
"""

n = int(input("Enter N: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
