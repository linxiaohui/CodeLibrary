#!/usr/bin/env python

from datetime import datetime
print datetime.now()

seq=[i*9*10**(i-1) for i in range(10)]
seq[0]=0

def DigitN(n):
    global seq
    acu=0
    i=0
    while n>acu+seq[i]:
        acu+=seq[i]
        i+=1
    margin = n-acu
    cnt = (margin+i-1)/i
    num = 10**(i-1)+cnt-1
    return int(str(num)[margin%i-1])

print reduce(lambda x,y:x*y, map(DigitN,[10**_ for _ in range(7)]))

print datetime.now()
