#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P010():
    LIMIT=2000000+1
    primes=[1]*LIMIT
    primes[0],primes[1]=0,0
    s,i=0,2
    while i<LIMIT:
        if primes[i]==1:
            s+=i
            ind=2
            while ind*i<LIMIT:
                primes[ind*i]=0
                ind+=1
        i+=1
    print s

print timeit.timeit(P010, number=1)
