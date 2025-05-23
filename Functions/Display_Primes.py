#Write a Program to Display Prime Numbers Between Two Intervals (entered by the user) Using Functions

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_primes(start, end):
    print("Prime numbers:", end=" ")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

start = int(input("Enter start: "))
end = int(input("Enter end: "))
display_primes(start, end)
