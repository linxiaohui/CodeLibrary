#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(str_number, radix):
    digits=[]
    for d in str_number:
    	if '0'<=d<='9':
    		digits.append(int(d))
    	else:
    		digits.append(ord(d)-ord('A')+10)
    digits.reverse()
    base=1
    ret=0
    for d in digits:
    	if d>=radix:
    		return -1
    	ret+=d*base
    	base*=radix
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
