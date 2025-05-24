#Q. Write a Program to Calculate Power of a Number without using inbuilt pow() function by taking two inputs from users as Base and exponent respectively

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = 1
for _ in range(exponent):
    result *= base
print("Result:", result)
