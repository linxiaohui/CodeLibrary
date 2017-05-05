#!/usr/bin/env python

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
    
p = Sieve(10)
print sum(p)


p = Sieve(2000000)
print sum(p)
