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

P = Sieve(1000000)

PRIMES=set(P)

def IsCircularPrime(p):
    l=list(str(p))
    for i in range(len(l)):
        l=l[1:]+l[:1]
        if int(''.join(l)) not in PRIMES:
            return False
    return True
    
cnt=0
for p in P:
    if IsCircularPrime(p):
        cnt+=1
    
print cnt

print datetime.now()
