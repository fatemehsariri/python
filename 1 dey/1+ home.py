a=int(input("Enter a:"))
sum=0
sum2=0
p=1
j=0
while a!=0:
    r=a%10
    if r!=0:
        sum=sum*10+r
    else:
        j=r+j
    #p=p*10
    a=a//10
while sum!=0:
    r_2=sum%10
    sum2=sum2*10+r_2
    sum=sum//10
print(sum2)
