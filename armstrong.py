a=int(input("enter the number: "))
count=0
d=a
e=a
c=0
while(a>0):
    a=int(a/10)
    count=count+1

while(d>0):
    f=d%10
    d=int(d/10)
    c=c+(pow(f,count))
if(c==e):
    print("the number is armstrong")
else:
    print("the number is not an armstrong number")
