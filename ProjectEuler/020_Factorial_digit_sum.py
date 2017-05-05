#!/usr/bin/env python

from datetime import datetime
print datetime.now()


print sum(map(int,str(reduce(lambda x,y:x*y,range(1,100+1)))))


print datetime.now()