


'''
total=0

for i in range (1, num+1):
    total+=i

print(total)

'''

def rec(num):
    if num==0:
        return 0
    return num + rec(num-1)
        


print(rec(5))
