#-*- coding:UTF-8 -*-
'''
WebVTT字幕转化为SRT字幕
'''
import sys
import os
import glob
from moviepy.config import get_setting

for f in glob.iglob(os.path.join(sys.argv[1], "**"), recursive=True):
    if f.lower().endswith('.vtt'):
        srt=f[:-4]+".srt"
        cmd = [get_setting("FFMPEG_BINARY"), "-i", '"{}"'.format(f), '"{}"'.format(srt)]
        cmdline = ' '.join(cmd)
        print(cmdline)
        os.system(cmdline)
