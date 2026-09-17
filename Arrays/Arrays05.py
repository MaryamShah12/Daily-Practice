'''
Sum of arrays
'''
#using normal loop
arr=[32,98,76,49,37,24,12,7]

total=0

for i in arr:
    total+=i

print(total)



def rec(arr,index, total):
    if index == len(arr):
        return total
    
    total+=arr[index]    
    return rec(arr,index+1, total)



print(rec(arr,0,0))