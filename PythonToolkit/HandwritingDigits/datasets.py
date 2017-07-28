# -*- coding:UTF-8 -*-

import math
import numpy as np
import cv2
import mahotas

def load_digits(dpath):
    data = np.genfromtxt(dpath, dtype='uint8', skip_header=True, delimiter=',')
    label = data[:,0]
    print(data.shape)
    data = data[:, 1:].reshape(data.shape[0], 28, 28)
    return (data, label)


def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (math.ceil(w * r), height)
    else:
        r = width / float(w)
        dim = (width, math.ceil(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

def deskew(image, width):
    (h, w) = image.shape[:2]
    moments = cv2.moments(image)
    skew = moments["mu11"] / moments["mu02"]
    M = np.float32([[1, skew, -0.5 * w * skew],[0, 1, 0]])
    image = cv2.warpAffine(image, M, (w, h), flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    image = resize(image, width=width)
    return image


def center_extent(image, size):
    (eW, eH) = size
    if image.shape[1] > image.shape[0]:
        image = resize(image, width = eW)
    else:
        image = resize(image, height = eH)
    extent = np.zeros((eH, eW), dtype = "uint8")
    offsetX = (eW - image.shape[1]) // 2
    offsetY = (eH - image.shape[0]) // 2
    extent[offsetY:offsetY + image.shape[0], offsetX:offsetX + image.shape[1]] = image
    CM = mahotas.center_of_mass(extent)
    if np.any(np.isnan(CM)):
        return extent
    (cY, cX) = np.round(CM).astype("int32")
    (dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
    M = np.float32([[1, 0, dX], [0, 1, dY]])
    extent = cv2.warpAffine(extent, M, size)
    return extent

