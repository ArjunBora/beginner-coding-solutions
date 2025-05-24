#Q. Write a Program takes two matrices of order r1*c1 and r2*c2 respectively. 
#Then, the program multiplies these two matrices (if possible) and displays it on the screen.

r1 = int(input("Enter number of rows for matrix 1: "))
c1 = int(input("Enter number of columns for matrix 1: "))
r2 = int(input("Enter number of rows for matrix 2: "))
c2 = int(input("Enter number of columns for matrix 2: "))

if c1 != r2:
    print("Cannot multiply these matrices")
else:
    print("Enter matrix 1:")
    matrix1 = [[int(input()) for _ in range(c1)] for _ in range(r1)]
    
    print("Enter matrix 2:")
    matrix2 = [[int(input()) for _ in range(c2)] for _ in range(r2)]
    
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print("Result:")
    for row in result:
        print(row)
