#!/usr/bin/env python

from datetime import datetime
print datetime.now()


LIMIT=11
CUR=0
primes=[2, 3, 5, 7]
number=primes[-1]+2
PRIMES=set([2,3,5,7])

def Truncatable(n):
    l=str(n)
    for i in range(1,len(l)):
        if int(l[i:]) not in PRIMES or int(l[:-i]) not in PRIMES:
            return False
    return True

import math

SUM=0

while CUR<LIMIT:
    c=False
    m=int(math.sqrt(number))
    for p in primes:
        if p>m:
            break
        if number%p==0:
            c=True
            break
    if not c:
        primes.append(number)
        PRIMES.add(number)
        if Truncatable(number):
            print number
            SUM+=number
            CUR+=1
    number+=2

print SUM
print datetime.now()
