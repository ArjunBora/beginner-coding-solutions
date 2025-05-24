"""
Q. Write a Program to Display Prime Numbers Between Two Intervals (entered by user)

Example:
Enter two numbers: 0 20
Prime numbers between 0 and 20 are:
2 3 5 7 11 13 17 19
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Prime numbers:", end=" ")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
