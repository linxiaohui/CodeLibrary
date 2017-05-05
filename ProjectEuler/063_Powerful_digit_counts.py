#!/usr/bin/env python

from datetime import datetime
print datetime.now()

'''
10**(N-1)<=X**N<10**N

X<10
(N-1)*ln10<=N*lnX ===> N<=ln10/(ln10-lnX)

'''

from math import log

f=lambda x:int(log(10)/(log(10)-log(x)))

cnt=0
for i in range(1,10):
    cnt+=f(i)

print cnt

print datetime.now()