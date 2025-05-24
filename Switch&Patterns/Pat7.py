#Hollow Full Pyramid

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(' ' * (n - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')
