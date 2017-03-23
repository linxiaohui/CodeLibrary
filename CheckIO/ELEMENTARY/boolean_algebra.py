#!/usr/bin/env python
# -*- coding:utf-8 -*-


import operator

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
FUNCS=(operator.and_, operator.or_, lambda x,y:operator.or_(operator.not_(x),y), operator.xor, lambda x,y:1 if x==y else 0)

def boolean(x, y, operation):
	cal=dict(zip(OPERATION_NAMES, FUNCS))
	return cal[operation](x,y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
