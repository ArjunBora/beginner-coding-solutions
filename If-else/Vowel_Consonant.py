#Q. Write a Program to Check Whether a Character is Vowel or Consonant

char = input("Enter a character: ").lower()
if char in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")
