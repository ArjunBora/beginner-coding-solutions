#Full Pyramid

n = int(input("Enter N: "))
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
