#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def Sieve(limit):
    primes=[]
    sieve=[1]*(limit+1)
    sieve[0] = 0
    sieve[1] = 0
    i = 2
    while i<=limit:
        if sieve[i] == 1:
            primes.append(i)
            j=2
            while i*j<=limit:
                sieve[i*j]=0
                j+=1
        i+=1
    return primes

p = Sieve(1000)

PRIMES=set(p)

import math
def IsPrime(n):
    if n in PRIMES:
        return True
    if n<=1:
        return False
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    for l in range(3,m+1,2):
        if n%l==0:
            return False
    PRIMES.add(n)
    return True

MAX=0
for b in p:
    for a in range(-999,1000):
        n=0
        k=n**2+a*n+b
        while IsPrime(k):
            n+=1
            k=n**2+a*n+b
        if MAX<n:
            MAX=n
            A,B=a,b

print A,B,A*B

print datetime.now()
