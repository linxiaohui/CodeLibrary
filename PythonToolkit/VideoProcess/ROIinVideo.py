# -*- coding: utf-8 -*-

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
    out.write_videofile(outpath)

if __name__ == "__main__":
    roi=(0,0,200,100)
    inpath = r"f:\x.mp4"
    tmppath = r"f:\tmp.avi"
    outpath = r"f:\out.mp4"
    VideoOnlyROI(inpath, tmppath, roi)
    print("Creating VideoOnly OK")
    CombineAudio(inpath, tmppath, outpath)
    print("Done")

