#Q. Write a Program to Find Factorial of a given number N (N is entered by user)

n = int(input("Enter N: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)
