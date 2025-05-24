#Q. Write a Program to Find the HCF of two numbers entered by user

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("HCF:", hcf(num1, num2))
