# -*- coding: utf-8 -*-

import sys
import os
import glob
import pickle
import imagehash
from PIL import Image

target_path = sys.argv[1]
fp = open(sys.argv[2],"wb")

db={}
i=1
print(target_path)

for f in glob.iglob(os.path.join(target_path, "**"), recursive=True):
    print(f)
    if f.lower().endswith(".jpg"):
        sys.stdout.write(' '*110+'\r')
        sys.stdout.write('{},{}\r'.format(i,f)) 
        i+=1
        try:
            img = Image.open(f)
            hsh = imagehash.dhash(img)
            if hsh in db:
                db[hsh].append(f)
            else:
                db[hsh]=[f]
        except:
            print("failed {}".format(f))
        


pickle.dump(db, fp)
fp.close()
