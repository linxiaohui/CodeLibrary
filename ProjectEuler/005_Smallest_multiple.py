#!/usr/bin/env python

def GCD(a, b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)

def GCD(a,b):
    (a,b) = (b,a) if a<b else (a,b)
    while(a%b!=0):
        a,b=b,a%b
    return b

a=1
for i in range(2,21):
    a=a*i/GCD(a,i)

print a