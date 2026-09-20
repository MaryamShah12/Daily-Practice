'''
Non-repeating elements in an array
'''

arr=[10, 20, 70, 90, 80, 20, 10, 20]
dict={}
for i in arr:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

for key, value in dict.items():
    if value==1:
        print(key)