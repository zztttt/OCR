from cv2 import cv2
import sys
import pytesseract
import os
from deal_pic2 import MirrorPlus
 
if __name__ == '__main__':
 
  if len(sys.argv) < 2:
    print 'Usage: python ocr_simple.py image.jpg'
    sys.exit(1)
    
  m = MirrorPlus(sys.argv[1])
  m.mirror1()

  father_path = os.path.abspath(os.path.dirname(os.getcwd()+os.path.sep+"."))+"/"
  img_save_path = father_path[0:father_path.find("Code")] + "/Code/savedPic/"
  # Read image path from command line
  path = sys.argv[1][0:sys.argv[1].find('.')+1] + "tif"
  imPath = img_save_path + "d.normal.exp" + path
  #imPath = img_save_path + sys.argv[1]
  #print(imPath)
     
  # Uncomment the line below to provide path to tesseract manually
  # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
  config = ('-l d --oem 1 --psm 3')
 
  # Read image from disk
  im = cv2.imread(imPath, cv2.IMREAD_COLOR)
  res_path = father_path[0:father_path.find("Code")] + "Result/result_" + sys.argv[1][0:sys.argv[1].find('.')+1] + "txt"
  #print(res_path)
  f = open(res_path, 'w')

  # Run tesseract OCR on image
  text = pytesseract.image_to_string(im, config=config)
  f.write(text)
  f.close()
  
  # Print recognized text
  print(text)
