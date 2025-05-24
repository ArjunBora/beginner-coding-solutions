"""
Q. Write a Program to Make a Simple Calculator to Add, Subtract, Multiply or Divide Using Switch case.
The program should takes an arithmetic operator (+, -, *, /) and two operands from a user and performs the operation on those two operands depending upon the operator entered by the user.
"""

def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter choice (1-4): "))
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    else:
        print("Invalid choice")

calculator()
