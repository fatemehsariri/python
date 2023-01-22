a=1
n=int(input("Enter n:"))
for i in range(1,n+1):
    print(a)
    if i%2!=0:
        a=a*2
    if i%2==0:
        a=a*2+1