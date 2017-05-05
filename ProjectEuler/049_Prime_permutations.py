#!/usr/bin/env python


from datetime import datetime
print datetime.now()

import itertools

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

p=Sieve(10000)
PRIMES=[_ for _ in p if _>1000]
PRIMES.sort()

import collections

def Permutations(a,b,c):
    ca=collections.Counter(str(a))
    cb=collections.Counter(str(b))
    cc=collections.Counter(str(c))
    return ca==cb and cb==cc

for p in PRIMES:
    if p+3330 in PRIMES and p+6660 in PRIMES:
        if Permutations(p,p+3330,p+6660):
            print p,p+3330,p+6660


print datetime.now()

