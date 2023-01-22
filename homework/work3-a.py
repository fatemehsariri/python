m=int(input("Enter m:"))

for i in range(0,m):
    a=int(input("Enter a:"))
    sum=0
    p=1
    while a!=0:
        r=a%10
        r=r+i
        if r>9:
            r=r%10
        sum=sum+r*p
        p=p*10
        a=a//10
    print(sum)