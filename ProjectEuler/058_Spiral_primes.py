#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import math

def IsPrime(n):
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    for l in range(3,m+1,2):
        if n%l==0:
            return False
    return True

SideLength=3
primes=[2,3,7]

NUM=9
STEP=4
LEFT=4

Length=3

while 1.0*len(primes)/(2*Length-1) > 0.1:
    Length+=2
    while NUM<=Length*Length:
        NUM+=STEP
        if IsPrime(NUM):
            primes.append(NUM)
        LEFT-=1
        if LEFT==0:
            STEP+=2
            LEFT=4

print Length

print datetime.now()
