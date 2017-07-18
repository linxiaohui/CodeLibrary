# -*- coding: utf-8 -*-

# 人脸识别的流程
#  1. 人脸检测(ROI)
#  2. 关键点检测(facial landmarks)
#  3. 描述子提取(face_descriptor, 128D向量)
#  4. 计算相似性(In general, if two face descriptor vectors have a Euclidean distance between them less than 0.6 then they are from the same person)


import sys
import os
import glob
import dlib
import numpy
import skimage.io
from colorama import init, Fore, Back, Style
import pickle

init(autoreset=True)

candidate_path = sys.argv[1]

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

index={}
cnt = 0
for f in glob.iglob(os.path.join(candidate_path, "**"), recursive=True):
    if f.lower().endswith(".jpg"):
        cnt+=1
        print("Processing the {}th file: {}".format(cnt,f))
        descriptors = numpy.zeros(128)
        try:
            img = skimage.io.imread(f)
            dets = detector(img, 1)
            print("Number of faces detected: {}".format(len(dets)))
            if len(dets)>0:
                shape = sp(img, dets[0]) #只取第一个
                face_descriptor = facerec.compute_face_descriptor(img, shape)
                descriptors = numpy.array(face_descriptor)
            index[f]=descriptors
        except Exception as e:
            print("error where processing {}".format(f))
            print(e)

fp=open("mm.pickle","wb")
pickle.dump(index, fp)
fp.close()
