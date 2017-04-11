# *-* coding:UTF-8 *-*

import pickle
import sys

fp=open("banner.p","rb")

banner=pickle.load(fp)
print(banner)
print((type(banner)))

for line in banner:
    for (p,s) in line:
        sys.stdout.write(p*s)
    print("")
