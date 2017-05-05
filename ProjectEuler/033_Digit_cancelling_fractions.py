#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def GCD(a,b):
    if a>b:
        a,b=b,a
    while a%b!=0:
        a,b=b,a%b
    return b

R=[]
N=1
D=1
for n in range(10,100):
    for d in range(n+1,100):
        setn=set(str(n))
        setd=set(str(d))
        if len(setn&setd)!=1:
            continue
        aftern=setn-setd
        afterd=setd-setn
        if len(aftern)==1 and len(afterd)==1:
            if int(aftern.pop())*d==int(afterd.pop())*n:
                if n%10==0 and d%10==0:
                    continue
                R.append((n,d))
                N*=n
                D*=d

print R

print N,D

print D/GCD(N,D)

print datetime.now()
