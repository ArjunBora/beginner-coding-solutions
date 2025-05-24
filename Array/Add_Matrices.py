#Q. Write a Program that adds two matrices using Multi- dimensional Arrays where the number of rows r and columns c is entered by user (Value of r and c < 100)

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

print("Enter matrix 1:")
matrix1 = [[int(input()) for _ in range(c)] for _ in range(r)]

print("Enter matrix 2:")
matrix2 = [[int(input()) for _ in range(c)] for _ in range(r)]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(c)] for i in range(r)]

print("Result:")
for row in result:
    print(row)
