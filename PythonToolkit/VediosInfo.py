#-*- coding:UTF-8 -*-
'''
计算一个目录下的视频的时长
'''
import sys
import os
import glob
import cv2

destdir="."
target = "mp4"

if len(sys.argv)>=2:
    destdir= sys.argv[1]

if len(sys.argv)>=3:
    target = sys.argv[2]

time_sec = 0

for f in glob.iglob(os.path.join(destdir, "**"), recursive=True):
    if f.lower().endswith(target):
        print(f)
        v = cv2.VideoCapture(f)
        time_sec += v.get(cv2.CAP_PROP_FRAME_COUNT)/v.get(cv2.CAP_PROP_FPS)

print(time_sec/60)