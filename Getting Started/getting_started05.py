

low=int(input("enter low level limit"))
high=int(input("enter high level limit"))

n=high-low+1


print(n/2*(2*(low)+(n-1)))



'''
def rec(low, high):
    start=low
    stop=high
    if start<=stop:
        return stop + rec(start,stop-1)
    else:
        return 0
    

print(rec(low,high))
'''