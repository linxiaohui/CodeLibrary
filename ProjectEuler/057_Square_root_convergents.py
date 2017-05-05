#!/usr/bin/env python
from datetime import datetime
print datetime.now()

from  sympy import *

one=Integer(1)
two=Integer(2)

r=one

cnt=0

for _ in range(1000+1):
    r=one+one/(one+r)
    x=simplify(r)
    numerator=numer(x)
    denominator=denom(x)
    if len(str(int(numerator))) > len(str(int(denominator))):
        cnt+=1

print cnt

print datetime.now()