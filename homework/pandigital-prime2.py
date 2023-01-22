a=int(input("Enter a:"))
b=a
d=a
while d!=0:
    r1=d%10
    c=0
    flag=1
    while b!=0:
        r2=b%10
        if r1==r2:
            c=c+1
        b=b//10
    if c>1:
        flag=0
        break
    d=d//10
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
