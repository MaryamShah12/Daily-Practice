'''
Sort First half in Ascending and Second half in descending order in Python
'''

arr=[19,65,32,46,55,91,12,73]
arr=sorted(arr)
mid=len(arr)/2
i=0
j=len(arr)-1
mynew=[]
while i<mid:
    mynew.append(arr[i])
    i+=1

while j>=mid:
    mynew.append(arr[j])
    j-=1

print(mynew)