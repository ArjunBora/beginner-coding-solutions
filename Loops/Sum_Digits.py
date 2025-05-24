#Q. Write a Program to display sum of all digits of a given Number N by user

num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num = num // 10
print("Sum of digits:", sum_digits)
