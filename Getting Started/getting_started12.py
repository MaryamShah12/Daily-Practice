'''
Find the Reverse of a Number in Python Language
We need to write a python code to reverse the given integer and print the integer. The typical method is to use modulo and divide operators to break down the number and reassemble again in the reverse order. Here are some of the methods to solve the above mentioned problems,

Method 1: Using Simple Iteration
Method 2: Using String Slicing
Method 3: Using Recursion
'''


#method 1

num=int(input("Enter a number"))
'''
ans=0
while num>0:
    ans=ans*10
    ans+=num%10
    
    num=num//10



print(ans)

'''

def rec_reverse(num, ans):
    if num==0:
        return ans

    ans=ans*10 + num% 10

    return rec_reverse(num//10,ans)

#print(x[::-1])