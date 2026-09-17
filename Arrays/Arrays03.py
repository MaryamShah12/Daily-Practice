'''
Smallest and Largest Element in an array using Python
'''
import math
max=-math.inf
mini=math.inf

arr=[32,98,76,49,37,24,12,7]
for i in arr:
    if i<mini:
        mini=i
    elif i>max:
        max=i

print(max)
print(mini)