#!/usr/bin/env python

from datetime import datetime
print datetime.now()

LIMIT=1000000

def IsPalindromic(s):
    l=list(s)
    r=l[::-1]
    return l==r
    

SUM=0
for i in range(1,LIMIT):
    if IsPalindromic(str(i)) and IsPalindromic(bin(i)[2:]):
        SUM+=i

print SUM

print datetime.now()
