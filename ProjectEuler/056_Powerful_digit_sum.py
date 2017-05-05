#!/usr/bin/env python

from datetime import datetime
print datetime.now()

MAX=0
N=0

for a in range(1,100):
    for b in range(1,100):
        n=a**b
        l=sum(map(int,list(str(n))))
        if MAX<l:
            MAX=l

print MAX

print datetime.now()