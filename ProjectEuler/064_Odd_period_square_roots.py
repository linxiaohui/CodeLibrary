#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def CountFraction():
    import sympy
    i=2
    cnt=0
    while i<=10000:
        if i%100==0: print i
        r = sympy.ntheory.continued_fraction.continued_fraction_periodic(0,1,i)
        if len(r)==2:
            if len(r[1])%2==1:
                cnt+=1
    i+=1
    print cnt   

import math
'''http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion'''
def GetFractionP(n):
    m=0
    d=1
    cnt=0
    r=set()
    a=int(math.sqrt(n))
    if a*a==n:
        return 0
    a0=a
    m2=d*a-m
    d2=(n-m2*m2)//d
    a2=(a+m2)//d2
    while (m2,d2,a2) not in r:
        r.add((m2,d2,a2))
        m2=d2*a2-m2
        d2=(n-m2*m2)//d2
        a2=(a0+m2)//d2
    return len(r)

cnt=0
for i in range(2,10000+1):
    if GetFractionP(i)%2==1:
        cnt+=1

print cnt

print datetime.now()