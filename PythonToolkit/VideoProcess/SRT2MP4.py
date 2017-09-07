# -*- coding: utf-8 -*-

'''
直接调用ffmpeg对mp4文件添加字幕(同名的SRT文件)
'''
import os
import sys
import time
import argparse
import glob
from moviepy.config import get_setting

##
## 解决报错`Fontconfig error: Cannot load default config file`
os.environ['FONTCONFIG_PATH']=os.path.split(os.path.realpath(__file__))[0]
##

def BurnSrtToMp4(inpath, outpath):
    os.chdir(inpath)
    flist = os.listdir(".")
    for f in flist:
        if f.lower().endswith('.mp4'):
            srt=f[:-4]+".vtt"
            #print(srt)
            try:
                os.mkdir(outpath)
            except:
                pass
            out=os.path.join(outpath,f)
            print(out)
            cmd = [get_setting("FFMPEG_BINARY"), "-i", '"{}"'.format(f), "-vf", 'subtitles="{}"'.format(srt), '"{}"'.format(out)]
            cmdline = ' '.join(cmd)
            print(cmdline)
            os.system(cmdline)
            #break
        else:
            if os.path.isdir(f) and not f.startswith("."):
                BurnSrtToMp4(f, os.path.join(outpath,f))
    os.chdir("..")

def main():
    parser = argparse.ArgumentParser(description='Burn WebVTT into MP4')
    parser.add_argument("inpath")
    parser.add_argument("outpath")
    args = vars(parser.parse_args(sys.argv[1:]))
    inpath = args['inpath']
    outpath = args['outpath']
    BurnSrtToMp4(inpath, outpath)
    print("Done")

if __name__ == "__main__":
    main()
