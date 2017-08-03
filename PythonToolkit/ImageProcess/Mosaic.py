#-*- coding:UTF-8 -*-
# 实现原理:把图像上某个像素点一定范围邻域内的所有点用邻域内随机选取的一个像素点的颜色代替

import cv2

#返回输入frame的roi区域进行马赛克化的图片
def domosaic(frame, roi, pixsize=5):
    x,y,w,h = roi
    ret = frame.copy()
    roi = ret[y:y+h,x:x+w]
    xstep = w//pixsize
    ystep = h//pixsize
    for i in range(ystep):
        for j in range(xstep):
            roi[i*pixsize:i*pixsize+pixsize,j*pixsize:j*pixsize+pixsize]=roi[i*pixsize+pixsize//2,j*pixsize+pixsize//2]
    ret[y:y+h, x:x+w] = roi
    return ret

def mosaic(inpath, title="Mosaic"):
    image = cv2.imread(inpath)
    width, height, color = image.shape
    cv2.namedWindow(title)

    def onMouse(evt, x, y, flags, param):
        if evt == cv2.EVENT_LBUTTONDOWN:
            param["drawing"]=True
            param["start_pos"]=(x,y)
        elif evt == cv2.EVENT_MOUSEMOVE and flags&cv2.EVENT_FLAG_LBUTTON:
            param["curr_pos"]=(x,y)
            if param["drawing"]:
                frame = cv2.rectangle(image.copy(), param["start_pos"], (x, y), (0, 255, 0), 0)
                cv2.imshow(title, frame)
        elif evt == cv2.EVENT_LBUTTONUP:
            (x1, y1)=param["start_pos"]
            (x2, y2)=param["curr_pos"]
            X=min(x1,x2)
            Y=min(y1,y2)
            W=max(x1-x2,x2-x1)
            H=max(y1-y2,y2-y1)
            frame = domosaic(image, (X,Y,W,H))
            frame = cv2.rectangle(frame, param["start_pos"], param["curr_pos"], (0, 255, 0), 0)
            cv2.imshow(title, frame)
            kvalue = cv2.waitKey(0)
            if  kvalue & 0xFF == ord('q'):
                cv2.destroyWindow(title)
            elif kvalue & 0xFF == ord('s'):
                cv2.imwrite(inpath+"mosaic.jpg", frame)

    param = {}
    cv2.setMouseCallback(title, onMouse, param)
    cv2.imshow(title, image)
    cv2.waitKey(0)


def unittest():
    frame = cv2.imread(r"f:\x.jpg")
    cv2.imshow("xx",domosaic(frame, (440,81,400,300)))
    cv2.waitKey(0)

def main():
    inpath = r"f:\x.jpg"
    mosaic(inpath)

if __name__ == "__main__":
    main()
