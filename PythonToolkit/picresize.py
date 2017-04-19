#-*- coding:UTF-8 -*-
'''
批量调整图片大小

Requirement: PIL
PIL doc: http://effbot.org/imagingbook/introduction.htm
About rotate & orientation: http://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image
Tested at Windows 8.1
'''

import os,sys
from PIL import Image
from PIL import ExifTags 
HOSTCODE='GBK'

def ResizeDir(curdir, destdir):
    curdir = curdir.decode(HOSTCODE)
    destdir = destdir.decode(HOSTCODE)
    files = os.listdir(curdir)
    for f in files:
        fulpath = curdir + os.sep + f
        destfile = destdir + os.sep + f
        if os.path.isfile(fulpath):
            print "resize file %s" % fulpath.encode('utf8')
            try:
                im = Image.open(fulpath)
            except Exception,e:
                print e
                continue
            if hasattr(im, '_getexif'): # only present in JPEGs
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation]=='Orientation':
                        break 
                e = im._getexif()       # returns None if no EXIF data
                if e is not None:
                    exif=dict(e.items())
                    if orientation in exif:
                        orientation = exif[orientation]
                    if orientation == 3:
                        im = im.transpose(Image.ROTATE_180)
                    elif orientation == 6:
                        im = im.transpose(Image.ROTATE_270)
                    elif orientation == 8:
                        im = im.transpose(Image.ROTATE_90)
            (w, h) = im.size
            w2=w
            h2=h
            if w > 1200 :
                w2= 1200
                h2=h*w2/w
            x=(w2,h2)
            out = im.resize(x,Image.ANTIALIAS)
            out.save(destfile, im.format)
        else:
            print "resize dir  %s" % fulpath.encode('utf8')
            os.makedirs(destfile)
            ResizeDir(fulpath.encode('utf8'), destfile.encode('utf8'))

def main():
    SRC=sys.argv[1]
    DEST=sys.argv[2]
    ResizeDir(SRC, DEST)

if __name__ == "__main__":
    HOSTCODE = "UTF-8"
    print HOSTCODE
    print sys.argv
    main()
