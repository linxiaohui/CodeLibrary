#!/usr/bin/env python

from datetime import datetime
print datetime.now()


import math

LIMIT=28123

AbundantMark=[0]*(LIMIT+1)

for n in range(12,LIMIT+1):
    m=int(math.sqrt(n))
    s=1
    for i in range(2,m+1):
        if n%i==0:
            s+=i
            if i*i!=n:
                s+=n/i
            if s>n:
                AbundantMark[n]=1
                break


s=0
for i in range(LIMIT+1):
    Abundant=False
    for j in range(2,i/2+1):
        if AbundantMark[j]==1 and AbundantMark[i-j]==1:
            Abundant=True
            break
    if not Abundant:
        s+=i


print s

print datetime.now()
