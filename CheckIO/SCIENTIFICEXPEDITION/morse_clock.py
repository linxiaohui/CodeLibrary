#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def morse(x):
    x=int(x)
    t=map(lambda x:'.' if x=='0' else '-', bin(x/10)[2:].rjust(3,'0'))
    o=map(lambda x:'.' if x=='0' else '-', bin(x%10)[2:].rjust(4,'0'))
    return "".join(t)+" "+"".join(o)


def checkio(time_string):
    hour,mini,seco = time_string.split(":")
    return morse(hour)[1:]+" : "+morse(mini)+" : "+morse(seco)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

