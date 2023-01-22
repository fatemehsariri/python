n=int(input("Enter n:"))
max=0                                 
sum=0                                 
for i in range(n):
    flag=1
    a=int(input("Enter a:"))
    a_prime=a                        
    s=0
    while a!=0:
        r=a%10                      
        for j in range(2,r//2+1):     
            if r%j==0:
                flag=0
                break
        if flag==1:                  
            s=r+s                     
        if s>=sum:                    
            sum=s
            max=a_prime
        a=a//10
print(max)


        