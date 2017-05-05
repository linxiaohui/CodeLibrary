#!/usr/bin/env python

for a in range(1,1000/3+1):
    for b in range(a+1, 1000/2):
        c=1000-a-b
        if c>b and a**2+b**2==c**2:
                print a,b,c
                print a*b*c
