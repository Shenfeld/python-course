def PrimeComposite(x):
    if x==0: 
        return False
    elif x==1: 
        return False
    elif x==2:
        return True
    for i in range(2,x): 
        if x%i==0:   
            return False
            break   
        if i==x-1:  
            return True
x = int(input())
for i in range (x):
    z = int(input())
    print(PrimeComposite(z))
