#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(first, second):
    s1=set(first.split(","))
    s2=set(second.split(","))
    s=list(s1.intersection(s2))
    s.sort()
    return ",".join(s)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
