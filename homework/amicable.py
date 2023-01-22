a=int(input("Enter a:"))
aa=a
b=int(input("Enter b:"))
bb=b
sa=0
sb=0
for i in range(1,a//2+1):
    if a%i==0:
        sa=sa+i

for j in range(1,b//2+1):
    if b%j==0:
        sb=sb+j

if sa==bb and sb==aa:
    print("Y")
else:
    print("N")