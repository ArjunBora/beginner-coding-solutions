#Inverted Full Pyramid

n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
