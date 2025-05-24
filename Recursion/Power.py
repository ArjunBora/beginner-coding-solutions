#Q. Write a Program that calculates the power of a number using recursion where base and exponent is entered by the user.

def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent-1)

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Result:", power(base, exponent))
