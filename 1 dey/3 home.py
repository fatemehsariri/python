a=int(input("Enter a:"))
num=9
flag=1
while a!=0 and flag==1:
    r=a%10
    if r>num:
        flag=0
        print("descending!")
    else:
        num=r
        a=a//10
if flag==1:
    print("ascending!")
