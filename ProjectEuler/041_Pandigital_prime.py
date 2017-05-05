#!/usr/bin/env python


from datetime import datetime
print datetime.now()

import itertools
import math

base=range(9,0,-1)

def IsPrime(n):
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    for l in range(3,m+1,2):
        if n%l==0:
            return False
    return True

cnt=0
cont=True
while cont:
    while sum(base)%3==0:
        base.remove(base[0])
    it = itertools.permutations(base, len(base))
    for i in it:
        n=int(''.join(map(str,list(i))))
        if IsPrime(n):
            print n
            cont=False
            break
    base.remove(base[0])

print datetime.now()