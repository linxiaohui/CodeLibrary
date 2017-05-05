#!/usr/bin/env python
from datetime import datetime
print datetime.now()

D=5
N=2
V=1
def GCD(n,d):
    while n%d!=0:
        n,d=d,n%d
    return d

result=set()

for d in range(1, 12000+1):
    n=d/2
    if d%2==0:
        n=n-1
    i=d/3+1
    while i<=n:
        c=GCD(d, i)
        result.add((i/c,d/c))
        i+=1

print len(result)

print datetime.now()