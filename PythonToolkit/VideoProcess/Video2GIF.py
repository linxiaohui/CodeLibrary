# -*- coding: utf-8 -*-

'''
将视频转换为GIF图片
'''
import os
import sys
import time
import argparse
import subprocess as sp
import cv2
from moviepy.editor import VideoFileClip

def Video2GIF(inpath, outpath, start, end, fps):
    inputv = VideoFileClip(inpath)
    if end is not None:
        inputv = inputv.subclip(start, end)
    else:
        inputv = inputv.subclip(start)
    inputv.write_gif(outpath, fps=fps)

def main():
    parser = argparse.ArgumentParser(description='Convert Video to GIF')
    parser.add_argument("inpath")
    parser.add_argument("outpath")
    parser.add_argument("--start")
    parser.add_argument("--end")
    parser.add_argument("--fps")
    args = vars(parser.parse_args(sys.argv[1:]))
    print(args)
    inpath = args['inpath']
    outpath = args['outpath']
    start = 0
    if args['start'] is not None:
        start  = int(args['start'])
    end = None
    if args['end'] is not None:
        end = int(args['end'])
    fps = 12
    if args['fps'] is not None:
        fps = int(args['fps'])

    print("Converting {} to {}".format(inpath, outpath))
    print("begin time {}".format(time.asctime()))
    Video2GIF(inpath, outpath, start, end, fps)
    print("begin time {}".format(time.asctime()))
    print("Done")


if __name__ == "__main__":
    main()
