#!/usr/bin/env python
# *-* coding:UTF-8 *-*

import datetime
def checkio(log_text):
    delta=datetime.timedelta(minutes=30)
    r={}
    lines=log_text.split("\n")
    for log in lines:
        start,name,url=log.split(";;")
        site='.'.join(url.split("/")[2].split('.')[-2:]).lower()
        name=name.lower()
        d=datetime.datetime(*map(int,start.split('-')))
        k=name+";;"+site
        if k in r:
            r[k].append(d)
        else:
            r[k]=[d]
    out=[]
    for k in r:
        log=r[k]
        start=log[0]
        pre=start
        last=datetime.timedelta(seconds=0)
        i=1
        for l in log[1:]:
            if l-pre<delta:
                last=l-start
                pre=l
                i+=1
            else:
                out.append((k,last.days*86400+last.seconds+1,i))
                start=l
                pre=start
                last=datetime.timedelta(seconds=0)
                i=1
        else:
            out.append((k,last.days*86400+last.seconds+1,i))
    out.sort()
    return '\n'.join(map(lambda x:x[0]+";;"+str(x[1])+";;"+str(x[2]), out))



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"