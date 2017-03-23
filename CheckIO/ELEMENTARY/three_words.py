#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
def checkio(words):
	r=words.split(" ")
	l=len(r)
	if l<3:
		return False
	for i in range(l):
		if re.search('[0-9]', r[i]) is None:
			cnt+=1
			if cnt==3:
				return True
		else:
			cnt=0
	return False
