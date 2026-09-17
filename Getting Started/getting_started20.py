
'''
Find the Factors of a Number in Python
Given an integer Number as input, the objective is to search for all the factors of the 
Given integer input. Therefore, we write a program to 
Find the Factors of a Number in Python Language.
'''
import math
num=int(input("Enter a number to know it factors"))
factors=[]

for i in range(1, int(math.sqrt(num))+1):
    if num%i==0:
        j=num//i
        factors.append(i)
        if i==j:
            continue
        else:
            factors.append(j)
        


print(factors)