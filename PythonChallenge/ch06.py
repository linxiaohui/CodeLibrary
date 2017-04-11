# *-* coding:UTF-8 *-*

import re
import os
import sys
import zipfile

nexter=re.compile("[0-9]+")
start="90052"

f=zipfile.ZipFile("channel.zip")
cont=True
while cont:
    n="%s.txt"%start
    c=str(f.read(n))
    i=f.getinfo(n)
    #sys.stdout.write(str(i.comment))
    print(i.comment.decode("UTF-8"),sep='',end='')
    nxt=nexter.findall(c)
    if nxt:
        start=nxt[0]
    else:
        cont=False


