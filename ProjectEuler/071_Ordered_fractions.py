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

for d in range(9,1000000+1):
    n=3*d/7
    if n*7==3*d:
        n=n-1
    if n*D>N*d:
        N,D=n,d
        #print N,D

print N/GCD(D,N)
print datetime.now()