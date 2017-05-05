#!/usr/bin/env python
from datetime import datetime
print datetime.now()


LIMIT=100

cnt=[[0]*LIMIT for _ in range(LIMIT)]

for i in range(LIMIT):
    cnt[i][0]=1
    cnt[i][i]=1
    for j in range(1,i):
        n=i-j
        k=0
        while k<=j:
            cnt[i][j]+=cnt[n-1][k]
            k+=1

print sum(cnt[LIMIT-1])-1

print datetime.now()