#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def Digits5Power(n):
    return sum(map(lambda x:int(x)**5,str(n)))
    
SUM=0
for i in range(2,9**5*6):
    if i==Digits5Power(i):
        SUM+=i

print SUM

print datetime.now()
