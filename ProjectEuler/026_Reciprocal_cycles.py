#!/usr/bin/env python

from datetime import datetime
print datetime.now()

from decimal import Decimal, getcontext

LIMIT=1000
V=0
MAX=0

for n in range(2,LIMIT):
    getcontext().prec = 2000
    x=str(Decimal(1)/Decimal(n))
    if len(x)<getcontext().prec+2:
        continue
    x = x[:-3]
    sep = x.split(x[-1])
    i=-3
    while sep[-2]!=sep[i]:
        i-=1
    i+=1
    cnt=0
    while i<=-2:
        cnt+=1+len(sep[i])
        i+=1
    if MAX<cnt:
        MAX=cnt
        V=n
        
print V,MAX
print datetime.now()

MAX=0
V=0
for n in range(2,LIMIT):
    loopcnt = 0
    numerator=1
    reminder=[1]
    quotient=[]
    while numerator!=0:
        numerator*=10
        quotient.append(numerator//n)
        numerator-=n*(numerator//n)
        if numerator==0:
            break
        if numerator in reminder:
            i=-1
            while reminder[i]!=numerator:
                i-=1
                loopcnt+=1
            loopcnt+=1
            break
        reminder.append(numerator)
    if MAX<loopcnt:
        MAX=loopcnt
        V=n

print V,MAX
print datetime.now()
