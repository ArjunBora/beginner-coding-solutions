"""
Q. Write a Program to Remove all Characters in a String Except Alphabets.
Example:
Enter a string: p2'r"o@gram84iz./
Output String: programiz
"""

string = input("Enter a string: ")
result = ''.join(ch for ch in string if ch.isalpha())
print("Result:", result)
