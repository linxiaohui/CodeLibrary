# *-* coding:UTF-8 *-*

import re

#EXACTLY

pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
data=open("03.data").read()


r=re.findall(pattern,data)
print(''.join(r))
