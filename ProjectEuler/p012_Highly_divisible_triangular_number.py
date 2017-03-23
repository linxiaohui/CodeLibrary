#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P012():
    import math
    def divisors(n):
        r=int(math.sqrt(n))+1
        s=set([1,n])
        for i in range(2,r):
            if n%i==0:
                s.add(i)
                s.add(n/i)
        return len(s)
    n=10
    while True:
        l=divisors(n*(n+1)/2)
        if l>500:
            print n*(n+1)/2
            break
        n=n+1


print timeit.timeit(P012, number=1)
