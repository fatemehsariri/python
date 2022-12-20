a=int(input("Enter a:"))
i=0
while a!=0:
    r=a%10
    if r==2 or r==3 or r==5 or r==7:
        i=i+1
    a=a//10
print(i)
