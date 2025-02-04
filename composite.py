a=int(input("enter the number:"))
b=int(input("enter the number:"))
count=0
count1=0

for x in range(a,b+1,1):
    count=0
    for i in range(1,x+1,1):
        if(x%i==0):
            count=count+1
        
    if(count==2):
        print(count1)
        count1=0
        print(x)
    if(count>=3):
        count1=count1+1
