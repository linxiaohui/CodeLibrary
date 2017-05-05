#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def Pcnt(P):
    SUM=0
    for a in range(1,P//3+1):
        for b in range(max(a,P//2-a),P//2+1):
            c=P-a-b
            A,B,C=a**2,b**2,c**2
            if A+B==C:
                SUM+=1
                break
            if A+B>C:
                break
    return SUM

P=0
MAX=0

for p in range(1,1000+1):
    m=Pcnt(p)
    if MAX<m:
        MAX=m
        P=p

print P,MAX

print datetime.now()
