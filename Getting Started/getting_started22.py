'''
Check Whether or Not the Number is a Strong Number in Python Language
Given an integer input, the objective is to check whether or not the given integer input is a 
Strong number or not using loops and recursion. 
In order to do so we’ll check if the number satisfies the definition of a Strong number mentioned below
'''

num=int(input("Enter a number"))

temp=num
total=0

while temp>0:
    fact=1
    j=temp%10
    for i in range(j,1,-1):
        fact*=i

    total+=fact
    temp=temp//10


if total==num:
    print("Number is a strong number")
else:
    print("not a strong number")