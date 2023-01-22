a=int(input("Enter a:"))
b=int(input("Enter b:"))
bb=b
while b!=0:
    r=a%b                             
    a=b                               
    b=r                                
print("gcd:",a)
lcm=(a*bb)//a
print("lcm:",lcm)