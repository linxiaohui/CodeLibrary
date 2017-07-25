# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

# 摄像头只能一个进程获取
camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#文件的名称，格式，帧率，帧大小，是否彩色
out = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))

#VideoCapture类的get()方法不能获取摄像头帧速率的准确值(总是返回0)
#print(camera.get(cv2.CAP_PROP_FPS))
print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT), camera.get(cv2.CAP_PROP_FRAME_WIDTH))

objLower = np.array([20, 20, 100], dtype = "uint8")
objUpper = np.array([100, 100, 200],dtype = "uint8")


while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    print(frame.shape)
    obj = cv2.inRange(frame, objLower, objUpper)
    obj = cv2.GaussianBlur(obj, (3, 3), 0)
    #print(obj.shape)
    #cv2.inRange的返回值是`a thresholded image`, 因此下面的函数会报错
    #gray = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)
    (_, cnts, _) = cv2.findContours(obj, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    cv2.imshow("Camera", frame)
    #写入文件中
    # out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()
