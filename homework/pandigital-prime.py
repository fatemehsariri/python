a=int(input("Enter a:"))
b=a
d=a
#n digit
c=0
n=0
while d!=0:
    d=d//10
    n=n+1
flag=1 
for i in range(1,n+1):
    while a!=0:
        r=a%10
        if r==i:
            c=c+1
        a=a//10
    if c>1:
        flag=0
        break
if flag==1:
    print("yes!it was pandigital")
    f=1
    for j in range(2,a//2+1):
        if a%j==0:
            f=0
            break
    if f==1:
        print("a is pandigital prime :D")

else:
    print("no :((((")
