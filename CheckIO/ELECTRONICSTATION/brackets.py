#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def checkio(expression):
    stack=[]
    match={u')':u'(',u']':u'[',u'}':u'{'}
    for i in expression:
        if i in "([{":
            stack.append(i)
        elif i in ")}]":
            if len(stack)==0:
                return False
            if stack.pop()!=match[i]:
                return False
    return len(stack)==0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"