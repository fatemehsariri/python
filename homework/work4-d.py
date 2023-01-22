n=int(input("Enter n:"))
a=int(input("Enter a:"))
sum=0
p=1
while a!=0:
    b=a%10**n
    s=0
    c=0                      
    while c!=n:               
        r=b%10
        s=s*10+r
        b=b//10
        c=c+1
    sum=sum+s*p               
    p=p*(10**n)
    a=a//10**n
print(sum)