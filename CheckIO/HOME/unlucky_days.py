#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

def checkio(year):
	cnt=0
	for i in range(1,13):
		d=datetime.date(year,i,13)
		if d.weekday()==4:
			cnt+=1
	return cnt

print checkio(2015)
print checkio(1986)
