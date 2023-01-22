num=int(input("1)palindrome /n2)change base "))
if num==1:
    a=int(input("Enter a:"))
    s=0
    while a!=0:
        r=a%10
        s=s*10+r
        a=a//10
    print(s)
if num==2:
    a=int(input("Enter a:"))
    b=int(input("Enter base:"))
    p=1
    s=0
    while a!=0:
        r=a%b
        s=s+r*p
        p=p*10
        a=a//b
    print(s)
