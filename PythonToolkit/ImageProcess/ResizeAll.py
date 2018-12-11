# -*- coding: utf-8 -*-

from PIL import Image
import os

def main(targetdir, destdir):
    files = os.listdir(targetdir)
    for f in files:
        im = Image.open(os.sep.join(targetdir, f))
        out = im.resize(x,Image.ANTIALIAS)
        out.save(os.sep.join(destdir, f), im.format)

if __name__=="__main__":
    targetdir = ""
    destdir = ""
    main(targetdir, destdir)


