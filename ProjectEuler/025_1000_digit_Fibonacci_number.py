#!/usr/bin/env python

from datetime import datetime
print datetime.now()

i=3
pre2=1
pre=1
cur=pre2+pre
while len(str(cur)) < 1000:
   i+=1
   pre2,pre=pre,cur
   cur=pre2+pre 

print i

print datetime.now()