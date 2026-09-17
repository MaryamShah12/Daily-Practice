'''
Frequency of Elements in an Array in Python
'''
from collections import Counter




arr=[19,31,2,54,37,2,58,19,2]
freq=Counter(arr)

print(freq[2])
'''
freq={}
for i in arr:
    if i not in freq:
        freq[i]=1
    elif i in freq:
        freq[i]+=1


print(freq)
'''



'''
check=[]

for i in arr:
    count=0
    
    for j in arr:
        if i==j:
            count+=1

    if i not in check and count>1:
        print(f" {i} and {count}")    

    check.append(i)
'''