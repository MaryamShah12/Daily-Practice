'''
Given an integer input, the objective is to check whether or not the given input variable is an Armstrong number. In order to do so, we check whether the sum of the digits of each number to the power the length of the number is equal to the number itself or not. If the number is the same as the original, it’s an Armstrong number. Mentioned below are a few of the Methods used to solve this problem,

Method 1: Using Iteration
Method 2: Using Recursion
'''




num=int(input("Enter a number"))
temp=num
power=len(str(num))
total=0
'''

while temp>0:
    total+=pow(temp%10,power)
    temp=temp//10

if total==num:
    print("armstrong number")
else:
    print("not a armstrong number")
    '''

def rec(num, total):
    if num==0:
        return total 
    total+=pow(num%10,power)
    return rec(num//0, total)