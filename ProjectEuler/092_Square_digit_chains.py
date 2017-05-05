#!/usr/bin/env python

from datetime import datetime
print datetime.now()


def Next(n):
    return sum(map(lambda x:int(x)**2,str(n)))

LIMIT=9**2*7
mark=[0]*(LIMIT+1)

cnt=0
i=1
while i<=LIMIT:
    n=Next(i)
    while n!=89 and n!=1:
        n=Next(n)
    if n==89:
        mark[i]=1
        cnt+=1
    i+=1

while i<10000000:
    if i%1000000==0: print i
    n=Next(i)
    if mark[n]==1:
        cnt+=1
    i+=1

print cnt

print datetime.now()