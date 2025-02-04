a=656
input=a
e=0
mul=10
while(a>0):
    mod=a%10
    a=int(a/10)
    e=mod+(mul*e)
if(e==input):
    print("the number is palindrome")
else:
    print("the number is not palindrome")
