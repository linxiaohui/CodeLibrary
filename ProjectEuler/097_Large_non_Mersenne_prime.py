#!/usr/bin/env python

from datetime import datetime
print datetime.now()

base=28433
expr=7830457

print (base*pow(2,expr,10**10)+1)%10**10

print datetime.now()