#!/usr/bin/python
#-*- coding:UTF-8 -*-
'''
/*
    A Tiny Server to Show all pic in a directory (to browse in a browser)
    Update: text, zip
*/
Requirement: tornado chardet
'''
import sys
import os
import zipfile
import socket
import hashlib
import base64  
import pickle
import glob
import imagehash
from PIL import Image
import dlib
import skimage.io


fp = open(sys.argv[1],"rb")
db = pickle.load(fp)
fp.close()

win = dlib.image_window()

for f in glob.iglob(os.path.join(sys.argv[2], "**"), recursive=True):
    if f.lower().endswith(".jpg") or f.lower().endswith(".jpeg") :
        print("Finding {}".format(f))
        img = Image.open(f)
        hsh = imagehash.dhash(img)
        if hsh in db:
            win.clear_overlay()
            win.set_image(skimage.io.imread(f))
            dlib.hit_enter_to_continue()
            for d in db[hsh]:
                print("Found {}".format(d))
                win.set_image(skimage.io.imread(d))
                dlib.hit_enter_to_continue()
        else:
            print("Not Found")