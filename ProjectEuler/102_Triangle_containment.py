#!/usr/bin/env python
from datetime import datetime
print datetime.now()

data=open("p102_triangles.txt").read().split('\n')


def Area(xa,ya,xb,yb,xc,yc):
    return abs((xa-xc)*(yb-ya)-(xa-xb)*(yc-ya))

cnt=0
for t in data:
    x1,y1,x2,y2,x3,y3=map(int,t.split(','))
    T=Area(x1,y1,x2,y2,x3,y3)
    T1=Area(x1,y1,x2,y2,0,0)
    T2=Area(x3,y3,x2,y2,0,0)
    T3=Area(x1,y1,x3,y3,0,0)
    if T1+T2+T3==T:
        cnt+=1

print cnt
print datetime.now()