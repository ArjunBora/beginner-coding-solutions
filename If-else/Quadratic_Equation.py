#Q. Write a Program which accepts coefficients of a quadratic equation from the user and displays the roots 
#(both real and complex roots depending upon the discriminant)

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {real}+{imag}i and {real}-{imag}i")
