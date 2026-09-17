'''
Perfect Number
A Number that can be represented as the sum of all the factors of the number is known as a Perfect Number.
'''
import math

num=int(input("Enter a number to know it is perfect number or not"))
factors=[]
for i in range(1, int(math.sqrt(num))+1):
    if num%i==0:
        factors.append(i)
        j=num//i
        if j==i or j==num:
            continue
        else:
            factors.append(j)

print(factors)
if sum(factors)==num:
    print("Perfect number")
else:
    print("Not a perfect number")