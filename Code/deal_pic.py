import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pip._internal
import copy
import sys, os

plt.switch_backend('agg')

class MirrorPlus():
    def __init__(self, filename, mode = 0):
        self.mode = mode
        self.filename = filename
        self.father_path = os.path.abspath(os.path.dirname(os.getcwd()+os.path.sep+"."))+"/"
        self.img_path = self.father_path[0:self.father_path.find("Code")] + "/Pic/"
        self.img_save_path = self.father_path[0:self.father_path.find("Code")] + "/Code/savedPic/"
        self.img = cv2.imread(self.img_path + self.filename)
        print("img_path", self.img_path)
        print("img_save_path", self.img_save_path)  
        #print("img", self.img)
    
    #plus the picture
    def Interpolation(self):
        img = copy.deepcopy(self.img)
        height,width,channels =img.shape
        emptyImage=np.zeros((500,1000,channels),np.uint8)
        sh=500.0/height#y
        sw=1000.0/width#x
        #img[y][x]
        for i in range(500):
            for j in range(1000):
                x=int(i/sh)
                y=int(j/sw)
                if x >= 128 or y >= 240:
                    print("ERRROR,", x, y, i, j)
                emptyImage[i,j]=img[x,y]
        kernel = np.ones((3,3))
        r = cv2.morphologyEx(emptyImage, cv2.MORPH_OPEN, kernel)
        return r
        cv2.imshow("111", emptyImage)
        #cv2.waitKey()
    def deleteBlank(self):
        maskX = []
        maskY = []
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                print(1)
    # mirror in Y
    def mirror1(self):
        #image.shape = (y, x)
        img = self.Interpolation()
        y = img.shape[0]
        x = img.shape[1]
        img2 = copy.deepcopy(img)
        #img[y][x]
        for i in range(x):
            for j in range(y):
                if self.mode == 0:
                    img2[j][i] = img[y - j - 1][i]
                elif self.mode == 1:
                    a = 1
        path = self.img_save_path + 'open' + self.filename[0:self.filename.find('.')+1] + "jpg"
        print(path)
        cv2.imwrite(path, img2)
        #cv2.imshow("111", img2)
        #cv2.waitKey()
#review code
def main():
    #m = MirrorPlus("1.bmp")
    #m = MirrorPlus("2.bmp", 1)
    #m = MirrorPlus("3.bmp")
    #m = MirrorPlus("4.bmp")
    #m = MirrorPlus("5.bmp")
    #m = MirrorPlus("6.bmp")
    #m = MirrorPlus("7.bmp")
    #m = MirrorPlus("8.bmp")
    #m = MirrorPlus("9.bmp")
    #m = MirrorPlus("10.bmp")
    
   
    m.mirror1()
    return 0
if __name__ == '__main__':
    main()
