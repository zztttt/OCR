# Image Preprocessing

### origin given images is small and mirrored, some characters are too thin to distinguish, and the number of images may not enough to tarin character set. So we preprocess the images with some mathematical morphology methods
1. Interpolation to enlarge the image
2. Open operation to thicken the character 
3. Mirror to invert image
4. Invertion the pixel values
5. Dilation and Erosion to make character easier to detect
6. Separation to recognition one line
7. Rotation to get more training data

# 


## Interpolation
Given images are in a small shape of (240 * 128) that may cause difficulties for recognition. We decide to execute interpolation operation to each images. 
We use a simple nearest neighbor interpolation which extend the image to the shape of (1000 * 500).
```
    sh=500.0/height#y
    sw=1000.0/width#x
    #img[y][x]
    for i in range(500):
        for j in range(1000):
            x=int(i/sh)
            y=int(j/sw)
            emptyImage[i,j]=img[x,y]
```
After that, we find the interpolated images are rough with a lot of edges and corners. To make edge smooth, we make a open operation after interpolation.
```
    kernel = np.ones((3,3))
    r = cv2.dilate(emptyImage, kernel)
```

## Mirror
Almost all given images to recognition is mirrored, we make symmetrical change in x-axis for each pixel. 
```
    y = img.shape[0]
    x = img.shape[1]
    img2 = copy.deepcopy(img)
    for i in range(x):
        for j in range(y):
            img2[j][i] = img[y - j - 1][i]
```

## Invertion
The origin background is black which seems hard for recognition, we invert all the pixel values for that. 
```
def invertBW(self, img2):
    img = copy.deepcopy(img2)
    y, x, c = img.shape
    for j in range(y):
        for i in range(x):
            img[j][i] = [255,255,255] - img[j][i]
    return img
```
Besides, there are some difference in the image like 'ERROR', 'The key F8'. So we make special attention for that, invert them back.
```
def invertLine(self, img2):
    img = copy.deepcopy(img2)
    y, x, c = img.shape
    # invert up ERROR
    for j in range(0, 31):
        for i in range(360, 640):
            img[j][i] = [255,255,255] - img[j][i]
```
After that, add a erosion operation thicking the character

## Split
Use Projection Detection Method, count the valid pixel on the x-axis. Then set a threshold of the count of pixels, if the count of pixels greater than the threshold, then mark this row for the valid row.
```
inLine = False
start = 0
    for i in range(height):
        if((not(inLine)) and (projection[i] > 5)):
            inLine = True
            start = i
        elif(i - start > 2 and projection[i] < 5 and inLine):
            inLine = False
            if (i - start > 2):
                print iW,start,i-start+2
                cj = img[start:i,0:width]
```

## Dilation, Erosion, Open
Dilation erosion and open operation thicken the thin character, which is used in above preprocess. We think appropriately thicken the character is helpful for recognition.

## Rotation
only five images given, we rotate each separated line or image, producing four images with four direction, which enlarge the tarin dataset. We thick it is useful when we attempt to train our own chracter set.
```
img = copy.deepcopy(self.img)
# rotate img and save to savePic
cv2.imwrite(self.save_path+"rot0_"+self.filename, np.rot90(img, 0), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite(self.save_path+"rot1_"+self.filename, np.rot90(img, 1), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite(self.save_path+"rot2_"+self.filename, np.rot90(img, 2), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite(self.save_path+"rot3_"+self.filename, np.rot90(img, 3), [int(cv2.IMWRITE_JPEG_QUALITY), 100])
```
