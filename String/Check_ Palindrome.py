#Q. Write a program to check if a given string is a Palindrome or not.

string = input("Enter a string: ")
clean_str = ''.join(ch.lower() for ch in string if ch.isalnum())
print("Palindrome" if clean_str == clean_str[::-1] else "Not Palindrome")
