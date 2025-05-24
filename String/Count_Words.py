"""
Q. Write a program to count all the words in a given string. Words must be separated by only one space

Example:
Sample Input: Siddharth Singh
Sample Output: number of words -> 2
"""

string = input("Enter a string: ")
words = string.split()
print("Number of words:", len(words))
