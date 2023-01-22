n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    a=int(input("Enter a:"))
    s=0
    p=1
    while a!=0:
        r=a%10
        if r!=0:
            s=s+r*p
            p=p*10
        a=a//10
    sum=sum+s
print(sum)
        