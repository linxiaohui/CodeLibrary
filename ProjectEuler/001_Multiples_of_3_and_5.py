#!/usr/bin/env python

print reduce(lambda x,y:x+y, [i for i in range(1000) if i%3==0 or i%5==0])