#!/usr/bin/env python

data=range(1,1+100)
print sum(data)**2 - reduce(lambda x,y:x+y*y, data)

