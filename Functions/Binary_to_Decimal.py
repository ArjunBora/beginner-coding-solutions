#Q. Write a Program to Convert Binary Number to Decimal manually by creating user-defined functions.

def binary_to_decimal(binary):
    decimal = 0
    for i, digit in enumerate(reversed(binary)):
        decimal += int(digit) * (2 ** i)
    return decimal

binary = input("Enter binary number: ")
print("Decimal:", binary_to_decimal(binary))
