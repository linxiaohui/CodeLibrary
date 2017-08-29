# -*- coding: utf-8 -*-

'''
直接调用ffmpeg进行视频区域的裁剪
'''
import os
import sys
import time
import argparse
import subprocess as sp

import cv2
from moviepy.editor import VideoFileClip
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

    def onMouse(evt, x, y, flags, param):
        if evt == cv2.EVENT_LBUTTONDOWN:
            param["drawing"]=True
            param["start_pos"]=(x,y)
            param["curr_pos"]=(x,y)
        elif evt == cv2.EVENT_MOUSEMOVE and flags&cv2.EVENT_FLAG_LBUTTON:
            param["curr_pos"]=(x,y)
            if param["drawing"]:
                frame = cv2.rectangle(preframe.copy(), param["start_pos"], (x, y), (0, 255, 0), 0)
                cv2.imshow("info", frame)
        elif evt == cv2.EVENT_LBUTTONUP:
            (x1, y1)=param["start_pos"]
            (x2, y2)=param["curr_pos"]
            X=min(x1,x2)
            Y=min(y1,y2)
            W=max(x1-x2,x2-x1)
            H=max(y1-y2,y2-y1)
            param["pos"]=(X,Y,W,H)
            frame = cv2.rectangle(preframe.copy(), param["start_pos"], param["curr_pos"], (0, 255, 0), 0)
            cv2.imshow("info", frame)
            kvalue = cv2.waitKey(0)
            if  kvalue & 0xFF == ord('q'):
                cv2.destroyWindow("info")
            elif kvalue & 0xFF == ord('s'):
                cv2.imwrite(outpath+"_jpg.jpg", frame)
                cv2.destroyWindow("info")
    param = {}
    param["pos"] = None
    cv2.setMouseCallback("info", onMouse, param)
    cv2.imshow("info", preframe)
    cv2.waitKey(0)
    print(param["pos"])
    if param["pos"] is not None:
        return param["pos"]
    else:
        return None

def SliceROI(inpath, roi, outpath, start=0):
    """
    Crop Video by Popen (ffmpeg)
    """
    x,y,w,h=roi
    cmd = [get_setting("FFMPEG_BINARY"), "-y", "-ss", str(start), "-i", '"{}"'.format(inpath),
           "-vf", "crop={}:{}:{}:{}".format(w,h,x,y),
           '"{}"'.format(outpath)]
    cmdline = ' '.join(cmd)
    print(cmdline)
    os.system(cmdline)
    '''
    popen_params = {"stdout": sp.PIPE,
                    "stderr": sp.PIPE,
                    "stdin": -3}
    if os.name == "nt":
        popen_params["creationflags"] = 0x08000000
    proc = sp.Popen(cmd, **popen_params)
    while proc.poll() == None:  
        #print(proc.stdout.readline())
        print(proc.stderr.readline().strip().decode())
    '''

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
