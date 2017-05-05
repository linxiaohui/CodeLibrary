#!/usr/bin/env python

from datetime import datetime
print datetime.now()

s=set()
for a in range(2,100+1):
    for b in range(2,100+1):
       s.add(a**b)

print len(s)
 
print datetime.now()
