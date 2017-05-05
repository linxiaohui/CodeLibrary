#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import math
def ProperDivisors(n):
    m=int(math.sqrt(n))
    d=[1]
    for i in range(2,m+1):
        if n%i==0:
            d.append(i)
            if i*i!=n:
                d.append(n/i)
    return sum(d)


def AmicableSum(LIMIT):
    cnt=0
    mark=[0]*(LIMIT+1)
    for i in range(1,LIMIT):
        if mark[i]==0:
            mark[i]=ProperDivisors(i)
        p=mark[i]
        if p<LIMIT:
            if mark[p]==0:
                mark[p]=ProperDivisors(p)
            if i==mark[p] and i!=p:
                cnt+=i
                print i,p
    return cnt
    
print AmicableSum(10000)

print datetime.now()