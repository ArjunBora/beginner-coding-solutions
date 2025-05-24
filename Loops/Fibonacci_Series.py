#Q. Write a Program to Display Fibonacci Series upto nth term (n is entered by user)

n = int(input("Enter N: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
