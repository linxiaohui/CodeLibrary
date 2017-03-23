#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P012():
    import math
    def divisors(n):
        l=2
        r=int(math.sqrt(n))+1
        for i in range(2,r):
            if n%i==0:
                l+=2
            if i*i==n:
                l-=1
        return l
    n=10
    while True:
        if n%2==0:
            if divisors(n/2)*divisors(n+1)>500:
                print n*(n+1)/2
                break
        else:
            if divisors((n+1)/2)*divisors(n)>500:
                print n*(n+1)/2
                break
        n=n+1

print timeit.timeit(P012, number=1)

"""As n and n+1 have no factors in common (except for the number 1)
one can multiply the factor counts in n/2 and n+1, or n and (n+1)/2 as,
to arrive at the factor count of the nth triangle number."""
