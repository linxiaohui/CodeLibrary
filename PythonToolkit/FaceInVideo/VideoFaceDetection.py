# -*- coding: utf-8 -*-

import cv2
import os

face_cascade = cv2.CascadeClassifier(os.sep.join([os.environ["OPENCVDATA"],'haarcascades','haarcascade_frontalface_default.xml']))

# 摄像头只能一个进程获取
camera = cv2.VideoCapture(0)

# 格式
#('P', 'I', 'M', '1') = MPEG-1 codec
#('M', 'J', 'P', 'G') = motion-jpeg codec
#('M', 'P', '4', '2') = MPEG-4.2 codec 
#('D', 'I', 'V', '3') = MPEG-4.3 codec 
#('D', 'I', 'V', 'X') = MPEG-4 codec 
#('U', '2', '6', '3') = H263 codec 
#('I', '2', '6', '3') = H263I codec 
#('F', 'L', 'V', '1') = FLV1 codec

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#文件的名称，格式，帧率，帧大小，是否彩色
out = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))

#VideoCapture类的get()方法不能获取摄像头帧速率的准确值(总是返回0)
#print(camera.get(cv2.CAP_PROP_FPS))
print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT), camera.get(cv2.CAP_PROP_FRAME_WIDTH))

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    print(frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    frameCopy = frame.copy()
    for (X, Y, W, H) in faces:
        #print(X, Y, W, H)
        cv2.rectangle(frameCopy, (X, Y), (X + W, Y + H),(0, 255, 0), 5)
    cv2.imshow("Camera", frameCopy)
    out.write(frameCopy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()
