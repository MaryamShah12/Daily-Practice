'''
Sorting elements of an Array by Frequency
'''
from collections import Counter

arr=[19,31,2,54,37,2,58,19,2]
freq=Counter(arr)

for i in freq.most_common():
    for j in range (0,i[1]):
        print(i[0])