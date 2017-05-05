#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def Pandigital(l):
    s=sum([len(str(_)) for _ in l])
    if s>9:
        return s
    s=set()
    for _ in l:
        s.update(set(list(str(_))))
    if '0' in s:
        return 10
    return len(s)

def FormPandigital(l):
    r=[]
    for _ in l:
        r.append(str(_))
    return int(''.join(r))

MAX=0

for m in range(1,100000):
    n=1
    r=[]
    while True:
        r.append(m*n)
        ret = Pandigital(r)
        if ret == 9:
            t=FormPandigital(r)
            if MAX<t:
                MAX=t
            break
        elif ret > 9:
            break
        n+=1

print MAX

print datetime.now()
