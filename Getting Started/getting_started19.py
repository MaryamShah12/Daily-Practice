
def rec(num,power):
    if power==1:
        return num
    return num*rec(num, power-1)


num=int(input("Enter a number"))
power=int(input("Enter it's power"))
ans=1

'''
for i in range(1,power):
    ans*=num*i
'''
print(rec(num,power))
