#!/usr/bin/env python

from datetime import datetime
print datetime.now()

S=set()

M=set(map(str,range(1,10)))

def IsPandigital(i,j,k):
    si,sj,sk=str(i),str(j),str(k)
    SS=set()
    if len(si)+len(sj)+len(sk)==9:
        for _ in si+sj+sk:
            SS.add(_)
        return SS==M
    return False


for i in range(1,1000):
    for j in range(i,10000):
        k=i*j
        if IsPandigital(i,j,k):
            print i,j,k
            S.add(k)

SUM=0
for s in S:
    SUM+=s

print SUM

print datetime.now()
