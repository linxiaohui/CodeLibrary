# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
def train_model(traindatadir):
    samples =  np.empty((0,100))
    responses = []
    keys = [i for i in range(48,58)]
    datas = os.listdir(traindatadir)
    for f in datas:
        im2 = cv2.imread(traindatadir+os.sep+f)
        im = cv2.resize(im2, None, fx=5,fy=5, interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
        # grayscale image
        # the threshold value which is used to classify the pixel values
        # Third argument is the maxVal which represents the value to be given if pixel value is more than the threshold value
        # (retval, thresholded image)
        retval, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
        
        # thresh: source image
        # cv2.RETR_LIST: contour retrieval mode
        # cv2.CHAIN_APPROX_SIMPLE: contour approximation method
        # return: image, contours and hierarchy
        _,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # sort contours
        contours = sorted(contours, key=lambda cnt: cv2.boundingRect(cnt)[0])
        for cnt in contours:
            if cv2.contourArea(cnt)<30:
                continue
            [x,y,w,h] = cv2.boundingRect(cnt)
            print(x,y,w,h)
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            cv2.imshow('norm',im)
            key = cv2.waitKey(0)
            if key == 27:  # (escape to quit)
                break
            else:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1,100))
                samples = np.append(samples,sample,0)
    responses = np.array(responses,np.float32)
    responses = responses.reshape((responses.size,1))
    np.savetxt('features.data',samples)
    np.savetxt('labels.data',responses)

if __name__ == "__main__":
    train_model("train")