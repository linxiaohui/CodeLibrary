#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import re

V={'A','E','I','O','U','Y'}
C={'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z'}

def W(s):
	s=s.upper()
	for i in range(len(s)-1):
		if s[i] in V and s[i+1] in V or s[i] in C and s[i+1] in C:
			return False
	return True

def checkio(text):
	cnt=0
	for w in re.split("[^a-zA-Z0-9]", text):
		if len(w)<=1 or re.search("[0-9]",w):
			continue
		elif W(w):
			cnt+=1
	return cnt

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(u"hello word"))
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"