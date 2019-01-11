import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from PIL import Image  
import sys, os
import copy

class rotatePic():
    def __init__(self, filename):
        self.filename = filename
        self.father_path = os.path.abspath(os.path.dirname(os.getcwd()+os.path.sep+"."))+"/"
        self.img_path = self.father_path + "Pic/"
        self.save_path = self.father_path + "Code/savedPic/"
        self.img = cv2.imread(self.img_path + self.filename)
        #print("img_path", self.img_path)
        #print("img_save_path", self.img_save_path)  
    def rotateAndSave(self):
        img = copy.deepcopy(self.img)
        cv2.imwrite(self.save_path+"rot0_"+self.filename, np.rot90(img, 0), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        cv2.imwrite(self.save_path+"rot1_"+self.filename, np.rot90(img, 1), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        cv2.imwrite(self.save_path+"rot2_"+self.filename, np.rot90(img, 2), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        cv2.imwrite(self.save_path+"rot3_"+self.filename, np.rot90(img, 3), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Usage: python rotate_pic.py [image.jpg]')
        sys.exit(1)
    img_path = sys.argv[1]
    rp = rotatePic(img_path)
    rp.rotateAndSave()

    #cv2.imwrite('rotate2.jpg', np.rot90(img), [int(cv2.IMWRITE_JPEG_QUALITY), 100])