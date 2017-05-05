#!/usr/bin/env python

def IsPrime(num):
    if num==2 or num==3:
        return True
    if num%2==0:
        return False
    f = 3
    while f < num:
        if num%f == 0:
            return False
        f+=2
    return True
    
def LargetsPrimeFactor(num):
    factors = []
    f = 2
    while f<=num:
        if num%f==0 and IsPrime(f):
            factors.append(f)
            num/=f
        f+=1
    return max(factors)

print LargetsPrimeFactor(2)
print LargetsPrimeFactor(3)
print LargetsPrimeFactor(13195)
print LargetsPrimeFactor(600851475143 )
