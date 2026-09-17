'''Find the Greatest of the Two Numbers in Python Language
Given two integer inputs, the objective is to find the largest number among the two integer inputs. In order to do so we usually use if-else statements to check which one’s greater. Here are some of the Python methods to solve the above mentioned problem.

Method 1: Using if-else Statements
Method 2: Using Ternary Operator
Method 3: Using inbuilt max() Function
'''

#solution1 

num1=int(input("Enter a number "))
num2=int(input("Enter a second number"))

print(f"{max(num1,num2)} is greater")












'''
def great(num1, num2):
    return num1 if num1>num2 else num2

print(f"{great(num1,num2)} is greater")
'''



'''
def great(num1, num2):

    if num1> num2:
        return num1
    elif num2>num1:
        return num2
    elif num1==num2
        return "Both numbers are equal"


print(f"{great(num1,num2)} is greater")
'''