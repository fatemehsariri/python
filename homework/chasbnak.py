n=int(input("enter n:"))
s=0
p=1
for i in range(1,n+1):
    a=int(input("enter a:"))
    while a!=0:
        r=a%10
        s=s+r*p
        p=p*10
        a=a//10
print(s)