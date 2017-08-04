# -*- coding: utf-8 -*-

'''
直接调用ffmpeg进行视频区域的裁剪
'''

import sys
import time
import argparse

import cv2
from moviepy.editor import VideoFileClip
from moviepy.tools import subprocess_call
from moviepy.config import get_setting

def VideoInfo(inpath, outpath, sec=10):
    inputv = VideoFileClip(inpath)
    fps = inputv.fps
    width, height = inputv.size
    print("fps={}".format(fps))
    print("width={}, height={}".format(width, height))
    #get_frame return RGB ?
    preframe = inputv.get_frame(sec)[:,:,[2,1,0]]
    cv2.namedWindow("info")
    def onMouse(evt, x, y, flag, param):
        if flag & cv2.EVENT_FLAG_LBUTTON:
            param["pos"]=(x,y)
            showframe = preframe.copy()
            height, width,color = showframe.shape
            showframe = cv2.line(showframe, (x,0),(x,height), (0,255,0),1)
            showframe = cv2.line(showframe, (0,y),(width,y), (0,0,255),1)
            cv2.putText(showframe, "x={},y={}".format(x,y), (width//2, height//2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
            cv2.imshow("info", showframe)
            kvalue = cv2.waitKey(0)
            if  kvalue & 0xFF == ord('q'):
                cv2.destroyWindow("info")
            elif kvalue & 0xFF == ord('s'):
                cv2.imwrite(outpath, preframe)
    param = {}
    param["pos"] = None
    cv2.setMouseCallback("info", onMouse, param)
    cv2.imshow("info", preframe)
    cv2.waitKey(0)
    print(param["pos"])
    if param["pos"] is not None:
        return (0, 0, param["pos"][0], param["pos"][1])
    else:
        return None

def SliceROI(inpath, roi, outpath, start=0):
    """
    Crop Video by Popen (ffmpeg)
    """
    x,y,w,h=roi
    cmd = [get_setting("FFMPEG_BINARY"), "-y", "-ss", str(start), "-i", inpath,
           "-vf", "crop={}:{}:{}:{}".format(w,h,x,y),
           outpath]
    
    subprocess_call(cmd)
    
def main():
    parser = argparse.ArgumentParser(description='Crop ROI of A Video File.')
    parser.add_argument("inpath")
    parser.add_argument("outpath")
    parser.add_argument("--sec")
    parser.add_argument("--start")
    args = vars(parser.parse_args(sys.argv[1:]))
    print(args)
    inpath = args['inpath']
    outpath = args['outpath']
    sec = 0
    if args['sec'] is not None:
        sec  = int(args['sec'])
    start = 0
    if args['start'] is not None:
        start = int(args['start'])

    print("Converting {} to {}".format(inpath, outpath))
    roi = VideoInfo(inpath, outpath,sec=sec)
    if roi is None:
        print("DID NOT SELECT ROI. Exiting...")
        return
    print("begin time {}".format(time.asctime()))
    SliceROI(inpath, roi, outpath, start=start)
    print("begin time {}".format(time.asctime()))
    print("Done")

if __name__ == "__main__":
    main()
