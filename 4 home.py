a=int(input("Enter a:"))
max=0
while a!=0:
    r=a%10
    if r>max:
        max=r
    a=a//10
print(max)
