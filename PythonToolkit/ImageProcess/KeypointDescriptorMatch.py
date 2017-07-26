# -*- coding: utf-8 -*-

import numpy as np
import cv2
import glob

def detect(img):
    descriptor = cv2.BRISK_create()
    (kps, descs) = descriptor.detectAndCompute(img, None)
    return (kps, descs)

def describe(img):
    descriptor = cv2.BRISK_create()
    (kps, descs) = descriptor.detectAndCompute(img, None)
    kps = np.float32([kp.pt for kp in kps])
    return (kps, descs)

def match(kpsA, featuresA, kpsB, featuresB):
    ratio = 0.7
    minMatches = 40
    matcher = cv2.DescriptorMatcher_create("BruteForce-Hamming")
    rawMatches = matcher.knnMatch(featuresB, featuresA, 2)
    matches = []
    for m in rawMatches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            matches.append((m[0].trainIdx, m[0].queryIdx))
    if len(matches) > minMatches:
        ptsA = np.float32([kpsA[i] for (i, _) in matches])
        ptsB = np.float32([kpsB[j] for (_, j) in matches])
        (_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)
        return float(status.sum()) / status.size
    return -1.0

def search(queryKps, queryDescs, imgpath):
    results = {}
    for p in imgpath:
        i = cv2.imread(p)
        gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        (kps, descs) = describe(gray)
        score = match(queryKps, queryDescs, kps, descs)
        results[p] = score
    if len(results) > 0:
        results = sorted([(v, k) for (k, v) in results.items() if v > 0],reverse = True)
    return results


    
def main(args):
    img = cv2.imread(args["query"])
    ###
    (kpt, desc) =detect(img) 
    bk_img = img.copy()
    out_img = img.copy()
    out_img = cv2.drawKeypoints(bk_img, kpt, out_img)
    cv2.imshow("Keypoint", out_img)
    cv2.waitKey(0)
    ###
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (queryKps, queryDescs) = describe(gray)
    results = search(queryKps, queryDescs, glob.glob(args["canidate"]+"/*.jpg"))
    if len(results) == 0:
        print("No Result")
    else:
        for (i, (score, path)) in enumerate(results):
            print("Sore {}".format(score))
            result = cv2.imread(path)
            cv2.imshow("Result", result)
            cv2.waitKey(0)
            # 特征点匹配
            matcher = cv2.BFMatcher()
            kpt_2, desc_2 = detect(result)
            matches = matcher.match(desc, desc_2)
            # 显示匹配结果
            out_img = cv2.drawMatches(img, kpt, result, kpt_2, matches, out_img)
            cv2.imshow("match", out_img)
            cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__=="__main__":
    args={}
    args["query"]=r"e:\x.jpg"
    args["canidate"]=r"e:\l"
    main(args)

