import math 


low=int(input("Enter a start point"))
high=int(input("Enter a end point"))


for j in range(low, high):
    if j==1:
        continue
    elif j==2:
        print(j)
    elif j%2==0:
        continue
    else:
        for i in range(3,int(math.sqrt(j))+1, 2):
            if j%i==0:           
                
                break
        else:
            print(j)