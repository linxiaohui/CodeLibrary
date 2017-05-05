#!/usr/bin/env python

from datetime import datetime
print datetime.now()

SUM=0
NUM=1
STEP=2
LEFT=4
while NUM<=1001*1001:
    SUM+=NUM
    NUM+=STEP
    LEFT-=1
    if LEFT==0:
       STEP+=2
       LEFT=4

print SUM

print datetime.now()
