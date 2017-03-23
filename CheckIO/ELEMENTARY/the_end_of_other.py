#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(words_set):
	words=list(words_set)
	for i in range(len(words)):
		for j in range(len(words)):
			if i!=j:
				if words[i].endswith(words[j]):
					return True
	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"