a=int(input("Enter a:"))
b=int(input("Enter b:"))
sum=0
p=1
while a!=0:
    r=a%10
    if r!=b:
        sum=sum+p*r
        p=p*10
    a=a//10
print(sum)
