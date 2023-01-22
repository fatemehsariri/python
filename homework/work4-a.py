m=int(input("Enter m:"))
n=int(input("Enter n:"))
a=int(input("Enter a:"))
if m>n:
    max=m
    min=n
else:
    max=n
    min=m
b=a//10**max                     
r=a%10**max                      
rr=r%10**(min-1)                  
s=(b*(10**(min-1)))+rr           
print(s)