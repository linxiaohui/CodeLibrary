#!/usr/bin/env python
from datetime import datetime
print datetime.now()

LIMIT=1000000
factor=[[] for _ in range(LIMIT+1)]


def phi(l,n):
    dem=reduce(lambda x,y:x*y,l,1)
    nor=reduce(lambda x,y:x*(y-1),l,1)
    return n*nor/dem

i=2
while i<=LIMIT:
    if len(factor[i])==0:
        j=1
        while j*i<=LIMIT:
            factor[i*j].append(i)
            j+=1
    i+=1

print datetime.now()

cnt=0
for d in range(2,LIMIT+1):
    n=phi(factor[d],d)
    cnt+=n
print cnt






print datetime.now()