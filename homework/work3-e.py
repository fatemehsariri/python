a1=1
a2=1

c=0
n=int(input("Enter n:"))
for i in range(3,n+1):
    an=a1+a2
    print(an)
    a1=a2
    a2=an
    flag=1
    for j in range(2,an//2+1):
        if an%j==0:
            flag=0
            break
    if flag==1:
            c=c+1
print(c)