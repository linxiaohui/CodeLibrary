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
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import chi2_kernel
import pickle

init(autoreset=True)

target_path = sys.argv[1]

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
descriptors = []

win = dlib.image_window()

img = skimage.io.imread(target_path)
dets = detector(img, 1)
target_descriptor = numpy.zeros(128)

# 假设目标图片只有一人
for k, d in enumerate(dets):
    shape = sp(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    target_descriptor = numpy.array(face_descriptor) 

fp = open("descriptors.pickle","rb")
index = pickle.load(fp)
fp.close()

for f, descriptors in index.items():
    for v in descriptors:
        dist_ = numpy.linalg.norm(v - target_descriptor)
        if dist_ < 0.4:
            print(Fore.GREEN+"Found match:{}. dist={}".format(f, dist_))
            img = skimage.io.imread(f)
            win.clear_overlay()
            win.set_image(img)
            dlib.hit_enter_to_continue()
