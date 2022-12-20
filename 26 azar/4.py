a=int(input("Enter a:"))
b=int(input("Enter b:"))
i=0
j=0
while a!=0:
    r=a%10
    if r==0:
        i=i+1
    a=a//10
while b!=0:
    r=b%10
    if r==0:
        j=j+1
    b=b//10
if i>j:
    print("i>j")
elif j>i:
    print("j>i")
else:
    print("i=j")
