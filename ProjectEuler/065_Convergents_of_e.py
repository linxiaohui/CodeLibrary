#!/usr/bin/env python
from datetime import datetime
print datetime.now()

from  sympy import *


def GetN(n):
    if n%3!=2:
        return 1
    else:
        return 2*(n//3+1)

one=Integer(1)

i=99
ni=Integer(GetN(i))
r=one/ni
i-=1
while i>=1:
    ni=Integer(GetN(i))
    r=one/(r+ni)
    i-=1
    
r=Integer(2)+r

n=numer(simplify(r))

print sum(map(int,str(n)))

print datetime.now()