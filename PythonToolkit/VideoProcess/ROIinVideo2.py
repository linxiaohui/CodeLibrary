# -*- coding: utf-8 -*-

import cv2
from moviepy.editor import *

def VideoInfo(inpath, outpath, sec=10):
    inputv = cv2.VideoCapture(inpath)
    i=0
    fps = int(inputv.get(cv2.CAP_PROP_FPS))
    width, height = int(inputv.get(cv2.CAP_PROP_FRAME_WIDTH)), int(inputv.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("fps={}".format(fps))
    print("width={}, height={}".format(width, height))
    frame = None
    while i<=sec*fps:
        preframe = frame
        grabbed, frame = inputv.read()
        if not grabbed:
            break
        i+=1
    cv2.namedWindow("info")
    def onMouse(evt, x, y, flag, param):
        if flag & cv2.EVENT_FLAG_LBUTTON:
            param["pos"]=(x,y)
            showframe = preframe.copy()
            height, width,color = showframe.shape
            showframe = cv2.line(showframe, (x,0),(x,height), (0,255,0),2)
            showframe = cv2.line(showframe, (0,y),(width,y), (0,0,255),2)
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

def SliceROI(inpath, roi, outpath):
    def get_roi(image):
        x,y,w,h=roi
        return image[y:y+h, x:x+w]
    clip = VideoFileClip(inpath)
    print("fps={}; duration={}".format(clip.fps, clip.duration))
    roiclip = clip.fl_image(get_roi)
    roiclip.write_videofile(outpath)

def main():
    inpath = r"f:\x.mp4"
    outpath = r"f:\out.mp4"
    roi = VideoInfo(inpath, outpath)
    if roi is None:
        print("DID NOT SELECT ROI. Exiting...")
        return
    SliceROI(inpath, roi, outpath)
    print("Done")

def getinfo():
    inpath = r"f:\x.mp4"
    outpath = r"f:\x.jpg"
    VideoInfo(inpath, outpath)

if __name__ == "__main__":
    main()