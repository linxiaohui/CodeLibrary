#!/usr/bin/env python

from datetime import datetime
print datetime.now()

data=open("p099_base_exp.txt").read().split('\n')
print len(data)
import math
MAX=0
i=1
I=1
while i<=len(data):
    base,exp = map(int, data[i-1].split(','))
    if math.log(base)*exp > MAX:
        MAX=math.log(base)*exp
        I=i
    i+=1
    
print I

print datetime.now()