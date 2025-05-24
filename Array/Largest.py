#Q. Write a Program that takes n element from user and displays the largest element of an array

n = int(input("Enter N: "))
arr = []
for _ in range(n):
    num = float(input("Enter number: "))
    arr.append(num)
print("Largest:", max(arr))
