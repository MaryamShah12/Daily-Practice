

def fact(num):
    ans=1
    for i in range(num,1,-1):
        ans*=i
    return ans

def rec(num):
    if num==1 or num==0:
        return 1
    return num * rec(num-1)

num=int(input("Enter a num to calculate factorial"))

if num<0:
    print("Factorial not possible")
elif num==1 or num==0:
    print(1)
else:
    print(rec(num))

