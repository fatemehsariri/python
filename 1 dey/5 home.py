j=0
i=0
flag=1
while flag==1:
    a=int(input("Enter a:"))
    if a==0:
        flag=0
    if a%2==0 and a!=0:
        j=j+1
print(j)
