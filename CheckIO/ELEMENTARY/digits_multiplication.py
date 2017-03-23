#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(number):
	prod=1
	while number!=0:
		if number%10!=0:
			prod*=number%10
		number/=10
	return prod

print checkio(123405)