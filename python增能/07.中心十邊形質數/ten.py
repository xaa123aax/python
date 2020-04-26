

def ten(n):
    i=1    
    while 5*(i*i+i)+1<=n:
        if 5*(i*i+i)+1==n:
            return True
        i=i+1
    return False

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True


for i in range(2, 10000):
    if ten(i) and prime(i):
        print(i)