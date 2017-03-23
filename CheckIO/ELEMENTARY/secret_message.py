#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
def find_message(text):
	r=[]
	for i in text:
		if i in string.uppercase:
			r.append(i)
	return ''.join(r)

