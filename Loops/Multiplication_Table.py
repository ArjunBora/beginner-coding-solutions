#Q. Write a Program to Generate Multiplication Table of a number (entered by the user) using a for loop.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
