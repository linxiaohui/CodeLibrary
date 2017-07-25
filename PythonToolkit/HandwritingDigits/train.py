# -*- coding:UTF-8 -*-

# 使用 `http://www.kaggle.com/c/digit-recognizer`数据, 提取HOG作为特征

from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from skimage import feature
import datasets

args = {}
args["dataset"] = r"F:\Data\Digit Recognizer\train.csv"
args["model"] = r"model.pickle"


(digits, labels) = datasets.load_digits(args["dataset"])
features=[]
for image in digits:
    image = datasets.deskew(image, 20)
    image = datasets.center_extent(image, (20, 20))
    hist = feature.hog(image, orientations = 18, pixels_per_cell = (10, 10), cells_per_block = (1, 1), transform_sqrt = True)
    features.append(hist)

model = LinearSVC(random_state = 42)
model.fit(features, labels)
joblib.dump(model, args["model"])

