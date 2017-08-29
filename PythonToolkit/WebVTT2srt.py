#-*- coding:UTF-8 -*-
'''
WebVTT字幕转化为SRT字幕
'''
import sys
import os
import glob


for f in glob.iglob(os.path.join(sys.argv[1], "**"), recursive=True):
    if f.lower().endswith('.vtt'):
        srt=f[:-4]+".srt"
        print(srt)
        with open(f,"rb") as fp:
            fw=open(srt,"wb")
            for line in fp:
                if line.strip()!=b"WEBVTT":
                    fw.write(line)
            fw.close()
