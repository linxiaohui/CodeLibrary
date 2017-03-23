#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(*args):
	if len(args)==0:
		return 0
	return max(args)-min(args)
