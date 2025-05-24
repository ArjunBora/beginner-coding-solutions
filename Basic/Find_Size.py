#Q. Write a Program to Find Size of int, float, double and char in your computer

import sys
print("Size of int:", sys.getsizeof(0), "bytes")
print("Size of float:", sys.getsizeof(0.0), "bytes")
print("Size of double:", sys.getsizeof(0.0), "bytes")  # Python uses float for both
print("Size of char:", sys.getsizeof('a'), "bytes")
