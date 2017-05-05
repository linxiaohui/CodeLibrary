#!/usr/bin/env python


from datetime import datetime
print datetime.now()

import math

n=144

while True:
    Hn=n*(2*n-1)
    p=int((1+math.sqrt(1+24*Hn)/6))
    if 3*p*p-p==2*Hn:
        t=int((-1+math.sqrt(1+8*Hn))/2)
        if t*t+t==2*Hn:
            print Hn
            break
    n+=1


print datetime.now()