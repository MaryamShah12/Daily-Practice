'''
Find the Prime Factors of a Number in Python
Given an integer input as the number, the objective is to 
Find all the Prime Factors of a the given integer input number. 
Therefore, we’ll write a program to Find the Prime Factors of a Number in Python Language.
'''
import math
num=int(input("Enter a number to know it prime factors"))
prime_factors=[]
if num%2==0:
    
    prime_factors.append(2)
    num=num//2
    while num%2==0:
        num=num//2




for i in range(3, int(math.sqrt(num))+1, 2):
    if num%i==0:
    
        prime_factors.append(i)
        num=num//i
        while num%i==0:
            num=num//i



prime_factors.append(num)
        
print(prime_factors)

