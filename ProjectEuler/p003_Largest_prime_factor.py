#!/usr/bin/env python
# -*- coding:utf-8 -*-

NUMBER=600851475143
#NUMBER=13195
factors=set()
f=2
while f<=NUMBER:
    if NUMBER%f==0:
        factors.add(f)
        NUMBER/=f
    else:
        f+=1
print max(factors)
