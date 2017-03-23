#!/usr/bin/env python
# -*- coding:utf-8 -*-  

import re
def checkio(data):
    if len(data)<10:
        return False
    if re.search('[A-Z]', data):
        if re.search('[a-z]',data):
            if re.search('[0-9]',data):
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
