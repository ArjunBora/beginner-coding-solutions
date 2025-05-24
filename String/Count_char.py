#Q. Write a Program to Find the Number of Vowels, Consonants, Digits and White Spaces in a String

string = input("Enter a string: ")
vowels = consonants = digits = spaces = 0

for ch in string.lower():
    if ch in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("White spaces:", spaces)
