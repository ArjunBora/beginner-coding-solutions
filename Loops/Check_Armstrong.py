#Q. Write a Program to check whether a number entered by the user is an Armstrong number or not.

num = input("Enter a number: ")
n = len(num)
sum_pow = sum(int(digit)**n for digit in num)
print("Armstrong" if sum_pow == int(num) else "Not Armstrong")
