#!/bin/python

import urllib.request
import re

urlpattern="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"
nexter=re.compile("[0-9]+")
starter=12345
starter=8022
starter=63579
index=0
cont=True
print("peak.html")
cont=False
while cont:
	url=urlpattern%starter
	print(url)
	fp=urllib.request.urlopen(url)
	content=fp.read()
	print(content)
	nextt=nexter.findall(str(content))
	print(nextt)
	nextor=int(nextt[0])
	if nextor==starter:
		cont=False
	starter=nextor

