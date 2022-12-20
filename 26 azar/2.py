a=int(input("Enter a:"))
sum=0
b=a
while a!=0:
    r=a%10
    sum=sum*10+r
    a=a//10
if sum==b:
    print("ok")
else:
    print("no")
