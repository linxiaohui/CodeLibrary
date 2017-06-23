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

candidate_path = sys.argv[1]
target_path = sys.argv[2]

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("g:\\shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("g:\\dlib_face_recognition_resnet_model_v1.dat")
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

for f in glob.iglob(os.path.join(candidate_path, "**"), recursive=True):
    if f.lower().endswith(".jpg"):
        print("Processing file: {}".format(f))
        img = skimage.io.imread(f)
        dets = detector(img, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            shape = sp(img, d)
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            v = numpy.array(face_descriptor)
            dist_ = numpy.linalg.norm(v-target_descriptor)
            if dist_ < 0.6:
                print("Found match: {}. dist={}".format(f, dist_))
                win.clear_overlay()
                win.set_image(img)
                win.add_overlay(d)
                dlib.hit_enter_to_continue()
