a=int(input("enter the number:"))
count=0
for x in range(1,a+1):
    if(a%x==0):
        count=count+1
if(count==2):
    print("the number is prime")
else:
    print("the number is not prime")
