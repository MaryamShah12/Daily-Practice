'''
Second Smallest Element in an array using Python
'''
import math

mini1=math.inf
mini2=math.inf

arr=[32,98,76,49,37,24,12,7]
'''
for i in arr:
    if mini1>i:
        mini1=i


for i in arr:
    if i>mini1 and i<mini2:
        mini2=i

print(mini2)
'''
#doing in single loop 

for i in arr:
    if i<mini1:
        mini2=mini1
        mini1=i
    elif i>mini1 and i<mini2:
        mini2=i


print(mini2)
print(mini1)
