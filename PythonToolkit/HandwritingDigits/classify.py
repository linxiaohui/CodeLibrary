# -*- coding:UTF-8 -*-
# 识别一张手写数字的图片中的数字
# 首先对图片进行处理, 通过`findContours`确定包含单个数字的`轮廓`
# 根据`轮廓`选取ROI, 通过之前训练的模型`predict`数字

from sklearn.externals import joblib
from skimage import feature
import numpy as np
import mahotas
import cv2
import datasets
import mahotas

args = {}
args["model"] = r"model.pickle"
args["image"] = r"o.jpg"

model = joblib.load(args["model"])
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 30, 150)
ret, edged = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY_INV)  
## 腐蚀与膨胀
#kernel = np.uint8(np.zeros((3,3)))
#gray = cv2.erode(gray, kernel)
#gray = cv2.dilate(gray, kernel)
cv2.imwrite("gray.jpg", edged)

## 试图使用轮廓加强一下
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(edged,cnts,-1,(255,255,255),5)  
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(edged,cnts,-1,(255,255,255),5)  

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])

for cnt, _  in cnts:
    [x,y,w,h] = cv2.boundingRect(cnt)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imwrite("x.jpg", edged)

for (c, _) in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    if w >= 7 and h >= 20:
        roi = gray[y:y + h, x:x + w]
        thresh = roi.copy()
        T = mahotas.thresholding.otsu(roi)
        thresh[thresh > T] = 255
        thresh = cv2.bitwise_not(thresh)
        thresh = datasets.deskew(thresh, 20)
        thresh = datasets.center_extent(thresh, (20, 20))
        #cv2.imshow("thresh", roi)
        #cv2.waitKey(0)
        hist = feature.hog(thresh, orientations = 18, pixels_per_cell = (10, 10), cells_per_block = (1, 1), transform_sqrt = True)
        digit = model.predict([hist])[0]
        print("number is: {}".format(digit))
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
        cv2.putText(image, str(digit), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
#cv2.imshow("image", image)
#cv2.waitKey(0)
cv2.imwrite("result.jpg", image)
cv2.destroyAllWindows()
