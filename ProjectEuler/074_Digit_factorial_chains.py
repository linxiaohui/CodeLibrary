#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from datetime import datetime
print datetime.now()

factor=[1]*10
for i in range(1,10):
    factor[i]=i*factor[i-1]

def factorial(n):
    return sum(map(lambda x:factor[x],map(int,str(n))))

LIMIT=20000

step={}

for i in range(1, LIMIT+1):
    cnt=set()
    cnt.add(i)
    k=factorial(i)
    while k not in cnt:
        cnt.add(k)
        k=factorial(k)
    step[i]=len(cnt)

print datetime.now()

i=LIMIT+1
while i<1000000:
    k=factorial(i)
    cnt=set()
    cnt.add(i)
    k=factorial(i)
    while True:
        if k in step:
            step[i]=len(cnt)+step[k]
            break
        if k in cnt:
            step[i]=len(cnt)
            break
        cnt.add(k)
        k=factorial(k)
    i+=1

cnt=0
for k in step:
    if step[k]==60:
        cnt+=1
        
print cnt

print datetime.now()