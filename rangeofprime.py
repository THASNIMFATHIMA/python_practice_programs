a=int(input("enter the number"))
b=int(input("enter the number"))
for x in range(a,b):
    count=0
    for y in range (1,x+1):
        if(x%y==0):
            count=count+1
    if(count==2):
        print(x)
