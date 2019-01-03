import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pip._internal
import copy


def main():
    filename = "2.jpg"
    path = "/home/zzt/OCR/OCR/Code/"
    path = path + filename
    path2 = "./Code/" + filename

    img =  cv2.imread(path, 0)
    #cv2.imshow("111",img)
    shape = img.shape
    img2 = copy.deepcopy(img)
    x = shape[0]
    y = shape[1]
    for i in range(x):
        for j in range(y):
            img[i][j] = img2[i][y-j-1]
    #need to optimized
    img3 = copy.deepcopy(img)
    for i in range(x):
        for j in range(y):
            img[i][j] = img3[x-i-1][y-j-1]
    #cv2.imshow("222", img)
    path = "/home/zzt/OCR/OCR/Code/"
    cv2.imwrite(path+"2.swp.jpg", img)
    #cv2.waitKey(0)
    print(img)
    return 0
main()
