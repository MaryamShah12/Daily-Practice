

term=int(input("Enter the nth term"))
first=0
second=1

for i in range(1,term):

    temp=first+second
    first=second
    second=temp

   

print(first)
