'''
Given an integer input the objective is to check whether or not the given integer number as an input is palindrome or not.

For a number to be a Palindrome, the number must be the same when reversed. If the number doesn’t match the reverse of itself, the number is not a Palindrome.

Method 1:  Using Simple Iteration.
Method 2: Using String Slicing.
Method 3: Using Recursion
Method 4:  Using Character matching
Method 5: Using Character matching updated
Method 6: Using Built-in reversed function
Method 7:  Building reverse one char at a time
Method 8: Using Flag and backward reading
Method 9: Bonus using backward slicing
We’ll discuss the above-mentioned methods in detail in the sections below. Don’t forget to check the blue box mentioned below for better understanding of the problem.
'''


'''
def rec(num, current):
    if num==0:
        return  current
    current=current*10 + num%10
    return rec(num//10, current)
'''
num=int(input("Enter a number"))
#reversed=rec(num,0)
temp=num
rever=0
count=0
'''
if num==reversed(num):
    print("palidrome")
else:
    print("a palidrome")

    '''

while temp > 0:
    rever=rever*10 + temp%10
    temp=temp//10
    count+=1

print(count)


if rever==num:
    print("palidrome")
else:
    print("not a palidrome")


