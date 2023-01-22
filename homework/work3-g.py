n=int(input("Enter n:"))
s=0
sum=0
mu=float(input("Enter mu:"))
for i in range(1,n+1):
    a=float(input("Enter a:"))
    s=(a-mu)*(a-mu)
    sum=sum+s
v=sum/n

print(v)