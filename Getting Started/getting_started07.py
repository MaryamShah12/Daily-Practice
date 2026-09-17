'''
Find the Greatest of the Three Numbers in Python Language
Given three integers as inputs the objective is to find the greatest among them. In order to do so we check and compare the three integer inputs with each other and which ever is the greatest we print that number. Here are some methods to solve the above problem.

Method 1: Using if-else Statements
Method 2: Using Nested if-else Statements
Method 3: Using Ternary Operator
'''

num1=int(input("Enter a number "))
num2=int(input("Enter a second number"))
num3=int(input("Enter a second number"))



def great(num1,num2,num3):

    #temp=num1 if num1>num2 else num2
    return num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3

'''
def great(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
    elif num2>num1:
        if num2>num3:
            return num2
    else:
        return num3

'''

'''
def great(num1, num2, num3):
    if num1>num2 and num1 > num3:
        return num1
    elif num2>num1 and num2> num3:
        return num2
    else:
        return num3
    
'''

print(f"{great(num1,num2,num3)} is greater")



