'''
Finding Maximum scalar product of two vectors in an array
'''
arr=[99,21,56,12]
arr=sorted(arr)
arr2=[19,11,7,3]
arr2=sorted(arr2)
ans=0
if len(arr)==len(arr2):
    for i in range(0,len(arr)):
        ans+=arr[i]*arr2[i]
    print(ans)
else:
    print("scalar product not possible")


