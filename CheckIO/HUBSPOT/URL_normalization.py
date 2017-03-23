#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def checkio(url):
    url=url.lower()
    url_parts=url.split("/")
    h=url_parts[2].split(":")
    host=None
    if len(h)==2 and h[1]=="80":
        host=h[0]
    else:
        host=url_parts[2]
    out=url_parts[0].lower()+"//"+host.lower()
    path=[]
    for p in url_parts[3:]:
        if p=='..':
            path.pop()
        elif p=='.':
            pass
        else:
            path.append(p)
    path='/'.join(path)
    r=[]
    i=0
    while i<len(path):
        if path[i]=='%':
            code=int(path[i+1]+path[i+2],16)
            if 0x41<=code<=0x5a or 0x61<=code<=0x7a or 0x30<=code<=0x39 or code in [0x2d,0x2e,0x7e,0x5f]:
                r.append(chr(code).lower())
            else:
                r.append('%')
                r.append(path[i+1].upper())
                r.append(path[i+2].upper())
            i=i+3
        else:
            r.append(path[i])
            i=i+1
    path=''.join(r)
    if path==".":
        path=""
    if len(path)>0:
        path='/'+path
    out=out+path
    if url.endswith('/') and not out.endswith('/'):
        out=out+'/'
    return out

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio(u"http://www.checkio.org/%cc%b1bac") ==\
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio(u"http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio(u"http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio(u"http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio(u"http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')