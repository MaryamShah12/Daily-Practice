

arr=[12,22,2]
arr=sorted(arr)
arr2=[17,1,6]
arr2=sorted(arr2, reverse=True)
ans=0


for i in range(0,len(arr)):
    ans+=arr[i]*arr2[i]

print(ans)