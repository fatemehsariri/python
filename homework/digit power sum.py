a=int(input("Enter a:"))
b=a
s=0
while a!=0:
    r=a%10
    s=s+r
    a=a//10
flag=1
i=1
while flag==1:
    num=s**i
    if num>=b:
        flag=0
        break
    i=i+1

if num==b:
    print(s,"^",i)
else:
    print("No")
