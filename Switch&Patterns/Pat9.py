#Pascal's Triangle

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    # Print leading spaces
    print(' ' * (n - i), end='')
    
    # First element is always 1
    num = 1
    for j in range(1, i + 1):
        print(num, end=' ')
        num = num * (i - j) // j  # Calculate next number
    print()
