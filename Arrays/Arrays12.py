'''
Python Program for Counting Distinct Elements
'''
arr=[10, 20, 40, 30, 50, 20, 10, 20,11]

uni={}
for i in arr:
    if i not in uni:
        uni[i]=1
    else:
        uni[i]+=1

print(len(uni))
