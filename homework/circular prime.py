a=int(input("Enter a:"))
flag=1
for i in range(3): #adad 3 raqami
    for j in range(2,a//2+1):
        if a%j==0:
            flag=0
            break
    if flag==0:
        break
    if flag==1:
        print(a)
    
    r=a%10
    a=a//10
    a=r*100+a
if flag==1:
    print("Yes")
else:
    print("No")

    
