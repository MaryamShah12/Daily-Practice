'''
Reverse an array
'''

start=0

arr=[32,98,76,49,37,24,12,7]

end=len(arr)-1

while start<end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start+=1
    end-=1


print(arr)