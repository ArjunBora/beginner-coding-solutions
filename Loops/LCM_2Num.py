#Q. Write a Program to Find LCM of two numbers entered by user

def lcm(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM:", (num1 * num2) // lcm(num1, num2))
