a=int(input("enter the number: "))
count=0
a=a+1
while(a>0):
    count=0
    for x in range(1,a+1):
        if(a%x==0):
            count=count+1
    if(count==2):
        print(x)
        break;
    else:
        a=a+1
