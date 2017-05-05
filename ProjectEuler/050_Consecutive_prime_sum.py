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

p = Sieve(1000000)
print len(p)
PRIMES=set(p)
V=[]
SUM=[0]
SUM.extend(list(p))
i=1
while i<len(SUM):
    SUM[i]+=SUM[i-1]
    i+=1
MAX=0
for i in range(len(p)):
    if i%10000==0: print i
    for j in range(i,len(p)):
        s=SUM[j+1]-SUM[i]
        if s>1000000:
            break
        if s in PRIMES:
            if MAX<j+1-i:
                MAX=j+1-i
                V=p[i:j+1]
print sum(V)

print datetime.now()