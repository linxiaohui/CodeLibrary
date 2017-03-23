#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P007():
    LIMIT=10001
    primes=[2,3]
    i=4
    while len(primes)<LIMIT:
        for p in primes:
            if i%p==0:
                break
        else:
            primes.append(i)
        i+=1
    print primes[-1]

print timeit.timeit(P007,  number=1)
