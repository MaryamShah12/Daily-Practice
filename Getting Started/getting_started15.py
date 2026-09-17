'''
Given two integer inputs as intervals high and low, the objective is to write a python code to check if the numbers lying within the given interval are Armstrong Numbers or not.

An Armstrong number or a Narcissistic number is any number that sums up itself when each of its digits is raised to the power of a total number of digits in the number. Let us try to understand this through the below example,

abcd… = an + bn + cn + dn + …
Where n is the order(length/digits in number)
'''

low=int(input("Enter low limit"))
high=int(input("Enter high limit"))

for i in range(low, high+1):
    temp=i
    power=len(str(i))
    ans=0
    while temp>0:
        ans+=pow(temp%10,power)
        temp=temp//10

    if i==ans:
        print(i)
        

