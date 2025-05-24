#Q. Write a Program to Check Whether a Number N entered by user is Palindrome or Not

num = int(input("Enter a number: "))
original = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print("Palindrome" if original == rev else "Not Palindrome")
