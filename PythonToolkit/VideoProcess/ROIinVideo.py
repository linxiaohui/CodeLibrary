# -*- coding: utf-8 -*-
import sys
import time
import cv2
from moviepy.editor import *

# 格式
#('P', 'I', 'M', '1') = MPEG-1 codec
#('M', 'J', 'P', 'G') = motion-jpeg codec
#('M', 'P', '4', '2') = MPEG-4.2 codec 
#('D', 'I', 'V', '3') = MPEG-4.3 codec 
#('D', 'I', 'V', 'X') = MPEG-4 codec 
#('U', '2', '6', '3') = H263 codec 
#('I', '2', '6', '3') = H263I codec 
#('F', 'L', 'V', '1') = FLV1 codec

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


def VideoOnlyROI(inpath, tmppath, roi):
    (x,y,w,h) = roi
    inputv = cv2.VideoCapture(inpath)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = int(inputv.get(cv2.CAP_PROP_FPS))
    width, height = int(inputv.get(cv2.CAP_PROP_FRAME_WIDTH)), int(inputv.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("fps={}".format(fps))
    print("width={}, height={}".format(width, height))
    #文件的名称，格式，帧率，帧大小，是否彩色
    out = cv2.VideoWriter(tmppath, fourcc , fps, (w,h))
    #out = cv2.VideoWriter(tmppath, -1 , fps, (w,h))
    while True:
        (grabbed, frame) = inputv.read()
        if not grabbed:
            break
        out.write(frame[y:y+h,x:x+w])
    inputv.release()
    out.release()
    cv2.destroyAllWindows()

def CombineAudio(inpath, temppath, outpath):
    audioclip = AudioFileClip(inpath)
    # or
    #videoclip = VideoFileClip(inpath)
    #audioclip = videoclip.audio
    videoclip = VideoFileClip(temppath)
    out = videoclip.set_audio(audioclip)
    out.write_videofile(outpath, verbose=False, progress_bar=False)


def main():
    inpath = r"f:\x.mp4"
    tmppath = r"f:\tmp.avi"
    outpath = r"f:\out.mp4"
    roi = VideoInfo(inpath, outpath)
    if roi is None:
        print("DID NOT SELECT ROI. Exiting...")
        return
    VideoOnlyROI(inpath, tmppath, roi)
    print("Creating VideoOnly OK")
    CombineAudio(inpath, tmppath, outpath)
    print("Done")


def getinfo():
    inpath = r"f:\x.mp4"
    outpath = r"f:\x.jpg"
    VideoInfo(inpath, outpath)

if __name__ == "__main__":
    print("begin time {}".format(time.asctime()))
    main()
    print("begin time {}".format(time.asctime()))