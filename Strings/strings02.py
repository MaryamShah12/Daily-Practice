'''
Check whether a character is an alphabet or not
'''

char=input("Enter a character")

if char.isalpha():
    print("correct input")
else:
    print(f"{char} this is not a character")