m=int(input("Enter m:"))
n=int(input("Enter n:"))
sum=0
p=1
while n!=0:
    r=n%10**m
    s=0
    while r!=0:
        r2=r%10
        s=s*10+r2
        r=r//10
    sum=sum+s*p
    p=p*10**m
    n=n//10**m
print(sum)
