for k in range(1,10000):
    sk=0
    sd=0
    for i in range(1,k//2+1): 
        if k%i==0:
            sk=sk+i
    
    for j in range(1,sk//2+1): 
        if sk%j==0:
            sd=sd+j 

    if k==sd and k!=sk:
        print(k,sk)
    