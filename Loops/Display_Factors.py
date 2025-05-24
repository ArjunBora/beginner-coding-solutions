#Q. Write a Program to Display all Factors of a Number entered by User

num = int(input("Enter a number: "))
print("Factors:", end=" ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
