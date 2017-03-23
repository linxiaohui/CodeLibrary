#!/usr/bin/env python
# -*- coding:utf-8 -*-

def count_words(text, words):
	text=text.lower()
	cnt=0
	for w in words:
		if text.find(w)>=0:
			print w
			cnt+=1
	return cnt

print count_words("How aresj you",{"how","are","you","hello"})