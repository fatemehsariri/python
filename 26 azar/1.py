a=int(input("Enter a:"))
i=0
while a!=0:
    r=a%10
    if r==2 or r==4 or r==6 or r==8 or r==0:
        i=i+1
    a=a//10
print(i)
