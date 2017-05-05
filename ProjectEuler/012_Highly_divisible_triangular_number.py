#!/usr/bin/env python

from datetime import datetime
import math
def Factors(n):
    m=int(math.sqrt(n))
    factors=2
    for i in range(2,m+1):
        if n%i==0:
            if i*i!=n:
                factors+=2
            else:
                factors+=1
    return factors

print datetime.now()
num = 1
n=num*(num+1)/2
factors=Factors(n)
while factors<500:
    #print num, factors
    num+=1
    n=num*(num+1)/2    
    factors=Factors(n)
    
print n
print datetime.now()