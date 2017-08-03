#-*- coding:UTF-8 -*-
# 实现原理:把图像上某个像素点一定范围邻域内的所有点用邻域内随机选取的一个像素点的颜色代替

import cv2

#返回输入frame的roi区域进行马赛克化的图片
def mosaic(frame, roi, pixsize=5):
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


def unittest():
    frame = cv2.imread(r"f:\x.jpg")
    cv2.imshow("xx",mosaic(frame, (440,81,400,300)))
    cv2.waitKey(0)

if __name__ == "__main__":
    unittest()
