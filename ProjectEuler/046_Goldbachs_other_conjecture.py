#!/usr/bin/env python
from datetime import datetime
print datetime.now()

import math

PRIMES=set([2,3])

def IsPrime(n):
    if n in PRIMES:
        return True
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    for l in range(3,m+1,2):
        if n%l==0:
            return False
    PRIMES.add(n)
    return True

n=35
cont=True
while cont:
    n+=2
    cont=False
    if IsPrime(n):
        cont=True
        continue
    else:
        i=1
        k=n-2*i**2
        while k>0:
            if IsPrime(k):
                cont=True
                break
            i+=1
            k=n-2*i**2

print n

print datetime.now()