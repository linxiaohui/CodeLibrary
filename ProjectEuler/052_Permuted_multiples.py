#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import collections

def Fitness(n):
    c=collections.Counter(str(n))
    i=2
    while i<=6:
        c2=collections.Counter(str(i*n))
        if c!=c2:
            return False
        i+=1
    return True

anchor=1
n=anchor
while not Fitness(n):
    n+=1
    if n>=2*anchor:
        anchor*=10
        n=anchor

print n

print datetime.now()