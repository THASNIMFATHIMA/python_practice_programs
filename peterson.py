a=145
count=0
c=1
d=0
input=a
while(a>0):
    b=a%10
    a=int(a/10)
    c=1
    
    
    for x in range(1,b+1):
        c=c*x
    d=d+c
if(input==d):
    print("the number is peterson number")
else:
    print("the number is not peterson number")
