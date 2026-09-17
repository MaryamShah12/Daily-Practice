'''
Largest Element in an array using python
'''

maxi=0
arr=[37, 77,54,89,22,36,95]
for i in arr:
    if i>maxi:
        maxi=i


print(maxi)

sorted_Arr=sorted(arr)
print(sorted_Arr[-1])

print(max(arr))