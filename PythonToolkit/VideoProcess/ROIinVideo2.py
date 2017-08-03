# -*- coding: utf-8 -*-

import sys
import cv2
from moviepy.editor import *

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
    def get_roi(image):
        x,y,w,h=roi
        return image[y:y+h, x:x+w]
    clip = VideoFileClip(inpath).subclip(start)
    print("fps={}; duration={}".format(clip.fps, clip.duration))
    roiclip = clip.fl_image(get_roi)
    roiclip.write_videofile(outpath)

def main():
    inpath = sys.argv[1]
    outpath = sys.argv[2]
    print("Converting {} to {}".format(inpath, outpath))
    roi = VideoInfo(inpath, outpath,sec=900)
    if roi is None:
        print("DID NOT SELECT ROI. Exiting...")
        return
    SliceROI(inpath, roi, outpath, start=120)
    print("Done")

def getinfo():
    inpath = r"f:\x.mp4"
    outpath = r"f:\x.jpg"
    VideoInfo(inpath, outpath)

if __name__ == "__main__":
    main()