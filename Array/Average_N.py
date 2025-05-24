#Q. Write a Program that takes N elements (max. value of N is 100 and N is the float number specified by user) from user, stores data in an array and Calculates the average of those numbers.

n = int(input("Enter N (max 100): "))
arr = []
for _ in range(n):
    num = float(input("Enter number: "))
    arr.append(num)
print("Average:", sum(arr)/n)
