
'''
first=0
second=1
temp=0
for i in range(1, 11):
    print(f"{first} ")
    temp=first+second
    first=second
    second=temp
    '''



def fab(first, second, stop, count):
    if count==stop:
        return
    else:
        print(first)
        return fab(second, first+second, stop, count+1)


ans=fab(0,1,20,1)