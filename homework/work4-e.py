a=int(input("Enter a:")) 
p=1
s=0
while a!=0: 
    r=a%2
    s=s+r*p
    p=p*10
    a=a//2
print("a in base 2 is :",s)
flag=1
for i in range(2,s//2+1): 
    if s%i==0:
        flag=0
        break
if flag==1:
    print("a in base 2 is a prime number")
else:
    print("a in base 2 is not a prime number")
