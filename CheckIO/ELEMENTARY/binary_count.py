#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(number):
    cnt=0
    while number!=0:
    	cnt+=number%2
    	number/=2
    return cnt

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
