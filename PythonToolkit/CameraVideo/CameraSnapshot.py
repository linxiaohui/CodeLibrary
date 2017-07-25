# -*- coding: utf-8 -*-

import cv2
import os

# 摄像头只能一个进程获取
camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    print(frame.shape)
    
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("output.jpg", frame)

camera.release()
cv2.destroyAllWindows()
