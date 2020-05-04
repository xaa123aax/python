# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=100


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True     

def ten(n):
    j=1
    while(5*(j*j+j)+1<=n):   
        if (n==5*(j*j+j)+1):
            return True
        j=j+1
    return False

for i in range(2, n + 1):  
    is_prime = prime(i)  
    is_ten=ten(i)
    if is_prime and is_ten:             
        print(i)
                