'''
Finding the smallest element of the array
'''
import math
mini=math.inf
arr=[32,98,76,49,37,24,12,7]

for i in arr:
    if i<mini:
        mini=i

print(mini)