"""
Q. Write a program to find the largest word in a given String.
Example:
Sample Input: Python is a general-purpose programming language.
Sample Output: programming
"""

string = input("Enter a string: ")
words = string.split()
largest = max(words, key=len)
print("Largest word:", largest)
