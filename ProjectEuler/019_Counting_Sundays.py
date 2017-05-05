#!/usr/bin/env python

from datetime import datetime
print datetime.now()

from datetime import date
cnt = 0
for y in range(1901,2000+1):
    for m in range(1,12+1):
       d = date(y, m, 1)
       if d.weekday()==6:
        cnt+=1
        
print cnt

print datetime.now()