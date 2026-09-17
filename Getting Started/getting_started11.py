'''
Find the sum of the Digits of a Number
Given a number as an input the objective is to calculate the sum of the digits of the number. We first break down the number into digits and then add all the digits to the sum variable. We use the following operators to break down the string,

Modulo operator %: We use this operator to extract the digits from the number.
Divide operator /: We use this operator to shorten the number after the digit has been extracted.
We use the above-mentioned operators to find the sum of the digits of the number. Here are some of the methods to solve the above-mentioned problem.

Method 0: Using String Extraction method
Method 1: Using Brute Force
Method 2: Using Recursion I
Method 3: Using Recursion II
Method 4: Using ASCII table
Method 5: Using map(), sum() and strip methods
Method 6: One Line recursive function
Method 7 : The cool method
'''

#method 0
'''
num=input("enter a number")
sum=0
for digit in num:
    sum+=int(digit)

print(sum)
'''
#method1 
'''
num=int(input("Enter a number"))
total=0
while num>0:
    current=num%10
    total+=current
    num=num//10



print(total)
'''


#num=int(input("Enter a number"))


'''
def rec(num,total):
    if num==0:
        return total
    total+=num%10
    return rec(num//10, total)


def rec(num):
    if num==0:
        return 0
    
    return num%10 + rec(num//10)
'''

numbers = ["1", "2", "3"]

result = map(int, numbers)

print(sum(result))