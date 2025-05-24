#Q. Write a Program that takes a matrix of order r*c from the user and computes the transpose of the matrix

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = [[int(input()) for _ in range(c)] for _ in range(r)]

transpose = [[matrix[j][i] for j in range(r)] for i in range(c)]

print("Transpose:")
for row in transpose:
    print(row)
