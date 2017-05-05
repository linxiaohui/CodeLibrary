#!/usr/bin/env python

from datetime import datetime
print datetime.now()

cnt=0

multi=lambda x,y:x*y
    
def C(n,k):
    r = reduce(multi,range(1,n+1),1)/reduce(multi,range(1,k+1),1)
    return r/reduce(multi,range(1,n-k+1),1)

for n in range(1,101):
    for i in range(0,n+1):
        if C(n,i)>1000000:
            cnt+=1

print cnt

print datetime.now()