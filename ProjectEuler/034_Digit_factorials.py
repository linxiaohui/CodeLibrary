#!/usr/bin/env python

from datetime import datetime
print datetime.now()

factor=lambda n:reduce(lambda x,y:x*y,range(1,n+1),1)
Fact=[factor(_) for _ in range(10)]
def Curious(n):
    return n==sum([Fact[int(_)] for _ in str(n)])
    
LIMIT=factor(9)*7
CNT=0
for i in range(3, LIMIT):
    if Curious(i):
        CNT+=i

print CNT

print datetime.now()
