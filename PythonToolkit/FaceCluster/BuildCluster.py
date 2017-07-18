# -*- coding: utf-8 -*-

# 根据Dlib计算所得的`描述子`, 使用KNN聚类

import numpy
from sklearn import cluster
import pickle


fp=open("mm.pickle","rb")
descriptor=pickle.load(fp)
fp.close()


fnames=[]
descriptors=[]

for f,d in descriptor.items():
    fnames.append(f)
    descriptors.append(d)

k_means = cluster.KMeans(n_clusters=203)
k_means.fit(descriptors) 

clusters={}

for i,l in enumerate(k_means.labels_):
    if l in clusters:
        clusters[l].append(fnames[i])
    else:
        clusters[l]=[fnames[i]]

fp=open("cluster.pickle","wb")
pickle.dump(clusters, fp)
fp.close()


