#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import math

digits=range(0,10)

def IsPentagonal(P):
    x=int((1+math.sqrt(1+24*P)))/6
    if 2*P==(3*x-1)*x:
        return True
    else:
        return False

n=1
cont=True
while cont:
    D=n*(3*n-1)/2
    i=1
    while i<n:
        K=D-i*(3*i-1)/2
        if IsPentagonal(K):
            P=D+i*(3*i-1)/2
            if IsPentagonal(P):
                print K
                cont=False
                break
        i+=1
    n+=1

print datetime.now()