a=int(input("Enter a:"))
sum=0
sum2=0
while a!=0:
    r=a%10
    if r==9:
        r=0
        sum=sum*10+r
    else:
        r=r+1
        sum=sum*10+r
    a=a//10
while sum!=0:
    p=sum%10
    sum2=sum2*10+p
    sum=sum//10
print(sum2)
