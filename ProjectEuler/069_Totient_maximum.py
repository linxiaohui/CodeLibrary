#!/usr/bin/env python
from datetime import datetime
print datetime.now()

#import sympy

def phi(l):
    nor=reduce(lambda x,y:x*y,l,1)
    dem=reduce(lambda x,y:x*(y-1),l,1)
    return (nor,dem)

MAXN=0
MAXD=1

N=0

#for n in range(1,1000000+1):
#    factor=list(sympy.factorint(n))
#    (nor,dem) = phi(factor)
#    if MAXN*dem<MAXD*nor:
#        (MAXD,MAXN)=(dem,nor)
#        N=n       
#print N

#####

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

pro=1
for x in p:
    if pro*x>1000000:
        break
    pro=pro*x

print pro

print datetime.now()