#!/usr/bin/env python
# -*- coding:utf-8 -*-  

import datetime

name=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def most_frequent(year):
	d=datetime.date(year,1,1).weekday()
	isLeap=year%400==0 or year%100!=0 and year%4==0
	if isLeap:
		if d==6:
			return [name[0],name[d]]
		else:
			return [name[d],name[d+1]]
	else:
		return [name[d]]

print most_frequent(2399)
print most_frequent(1152)
print most_frequent(56)
print most_frequent(2909)