#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from datetime import datetime
print datetime.now()

'''Euler's totient function:
    ¦Õ(n)=n(1-1/p1)(1-1/p2)...(1-1/pn)'''

import math
def Totient(dd, nn):
    primes=[2,3]
    PRIMES=set(primes)
    D=3
    N=1
    number=primes[-1]
    while True:
        D=reduce(lambda x,y:x*y, primes)
        N=reduce(lambda x,y:x*(y-1),primes,1)
        if N*dd<D*nn:
            k=1
            while True:
                if k*N*dd<nn*(k*D-1):
                    print k*D
                    break
                k+=1
            break
        number+=2
        IsPrime=True
        m=int(math.sqrt(number))
        for p in primes:
            if p>m: break
            if number%p==0:
                IsPrime=False
                break
        if IsPrime:
            primes.append(number)
            PRIMES.add(number)

Totient(10,4)
Totient(94744, 15499) 

print datetime.now()