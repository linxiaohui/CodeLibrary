#!/usr/bin/env python

from datetime import datetime
print datetime.now()

data=open("p042_words.txt").read()
words=eval("["+data+"]")

def WordValue(w):
    val=0
    for c in w:
        val+=ord(c)-ord('A')+1
    return val


import math

def IsTriangle(n):
    m=int((-1+math.sqrt(1+8*n))/2)
    return m*(m+1)/2==n


cnt=0
for w in words:
    n=WordValue(w)
    if IsTriangle(n):
        cnt+=1

print cnt


print datetime.now()