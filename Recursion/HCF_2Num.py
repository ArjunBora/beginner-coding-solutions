#Q. Write a Program to Find HCF of two numbers entered by user Using Recursion

def hcf(a, b):
    return a if b == 0 else hcf(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("HCF:", hcf(num1, num2))
