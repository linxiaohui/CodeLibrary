#!/usr/bin/env python
# -*- coding:utf-8 -*-  
from collections import Counter

def checkio(data):
    cnter=Counter(data)
    s={c for c in cnter if cnter[c]>1}
    return [i for i in data if i in s]

if __name__ == "__main__":
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"