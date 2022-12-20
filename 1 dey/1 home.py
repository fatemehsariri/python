a=int(input("Enter a:"))
sum=0
p=1
while a!=0:
    r=a%10
    if r!=0:
        sum=sum+p*r
        p=p*10
    a=a//10
print(sum)
