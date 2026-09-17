'''
Check whether a character is a vowel or consonant
'''

vowels=["a", "e", "i", "o", "u"]

char=input("Enter the character")

if char.lower() in vowels:
    print("it is vowel")
else:
    print("it's a consonant")