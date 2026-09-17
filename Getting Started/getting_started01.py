def check(num):
    if not isinstance(num, (int, float)):
        return "invalid input"
    
    if num<0:
        return "negative"
    elif num==0:
        return "Zero"
    return "positive"

try:
    num=int(input("Enter a number."))
    print(check(num))

except :
    print("enter valid input")




