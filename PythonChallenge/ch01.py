#!/bin/python

import string

data="""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """

#transtab=string.maketrans("koe","mqg")
#print data.translate(transtab)

r=[]
for i in data:
	if i=='y':
		r.append('a')
	elif i=='z':
		r.append('b')
	elif i>='a' and i<='x':
		r.append(chr(ord(i)+2))
	else:
		r.append(i)

print(''.join(r))


'''
table = string.maketrans(
...   string.ascii_lowercase,
...   string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
'''

'''
for x in s:
    print  chr(ord(x) if ord(x)+2 < ord('a') else  ord(x)+2 if ord(x)+2 < ord('z') else ord(x)-24 ),
'''
