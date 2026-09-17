'''
Find the Longest Palindrome in an Array
'''

def ispalidrome(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False

def checklen(arr):
    leng=0
    ans=0
    for i in arr:
        
        if ispalidrome(i):
            if len(str(i))>leng:
                leng=len(str(i))
                ans=i
    return ans
            



arr = [1, 232, 5545455, 909090, 161]

print(checklen(arr))