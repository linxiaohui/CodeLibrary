#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import itertools
import string

data=eval("["+open("p059_cipher.txt").read()+"]")

def Decrypt(data, p):
    key=[ord(p[0]),ord(p[1]),ord(p[2])]
    plain=[]
    i=0
    while i<len(data):
        var=data[i]^key[i%3]
        plain.append(chr(var))
        if chr(var) not in string.printable:
            return False
        if chr(var) in ['#','@','}','{','%','/','`']:
            return False
        i+=1
    return ''.join(plain)

R=[]
for a in list(string.ascii_lowercase):
    for b in list(string.ascii_lowercase):
        for c in list(string.ascii_lowercase):
            p = (a,b,c)
            r = Decrypt(data, p)
            if r:
                print (a,b,c), r
                R=r
print sum(map(ord,R))

print datetime.now()