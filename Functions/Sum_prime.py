"""
Q.  Write a Program to check if an integer (entered by the user) can be expressed as the sum of two prime numbers,if yes then 
print all possible combinations with the use of functions.

Example
Enter a positive integer: 34
OUTPUT:
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(num):
    for i in range(2, num//2 + 1):
        if is_prime(i) and is_prime(num - i):
            print(f"{num} = {i} + {num-i}")

num = int(input("Enter a positive integer: "))
prime_sum(num)
