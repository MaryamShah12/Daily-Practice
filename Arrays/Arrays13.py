'''
Finding Repeating elements in an Array
'''


arr=[10, 20, 40, 30, 50, 20, 10, 20]

uniq={}
for i in arr:
    if i not in uniq:
        uniq[i]=1
    else:
        uniq[i]+=1


for key, value in uniq.items():
    if value >1:
        print(key)