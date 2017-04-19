# -*- coding: utf-8 -*-

import cv2
import numpy as np

samples = np.loadtxt('features.data',np.float32)
responses = np.loadtxt('labels.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
model.train(samples,cv2.ml.ROW_SAMPLE, responses)

im2 = cv2.imread('data.png')
im = cv2.resize(im2, None, fx=5,fy=5, interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

# RETR_EXTERNAL: 搜索最外层的轮廓，而不关注内部可能出现的任何轮廓
_, contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
result=""
# 轮廓检测时, 不一定按照图中顺序进行检测
contours = sorted(contours, key=lambda cnt: cv2.boundingRect(cnt)[0])
for cnt in contours:
    if cv2.contourArea(cnt)>30:
        [x,y,w,h] = cv2.boundingRect(cnt)
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        # ROI(region of interest)
        roi = thresh[y:y+h,x:x+w]
        roismall = cv2.resize(roi,(10,10))
        roismall = roismall.reshape((1,100))
        roismall = np.float32(roismall)
        retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
        #print(results,type(results),results.shape)
        result+=str(int((results[0][0])))
print(result)
