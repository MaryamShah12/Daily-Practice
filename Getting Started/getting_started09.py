import math

num=int(input("Enter a number"))



if num==1:
    print("Not a  prime number")
elif num==2:
    print("prime number")
elif num%2==0:
    print("Not a prime number")
else:
    for i in range(3,int(math.sqrt(num))+1, 2):
        if num%i==0:           
            print("Not a prime number")
            break
    else:
        print("Prime number")


    
    


def prime_number(num, divisor):
    if num==1:
        return False
    elif num==2:
        return True
    elif num%2==0:
        return False
    elif divisor> int(math.sqrt(num)):
        return True
    elif num%divisor==0:
        return False
    else:
        return prime_number(num, divisor+2)

ans=prime_number(num,3)

if ans:
    print("it is a prime number")
else:
    print("not a prime number")

                        
    
        
        
            



