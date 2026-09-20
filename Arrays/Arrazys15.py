'''
Removing Duplicates elements from an array
'''

arr=[10, 20, 70, 90, 80, 20, 10, 20]
#better approach without extra space
for ind, i in enumerate(arr):
    for j in range(len(arr)-1,ind,-1):
        if i==arr[j]:
            arr.pop(j)


print(arr)



'''
temp={}
for i in arr:
    if i not in temp:
        temp[i]=1
    else:
        temp[i]+=1


for key,value in temp.items():
    if value>1:
        arr.remove(key)


print(arr)
'''

