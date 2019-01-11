# Image Preprocessing

### origin given images is small and mirrored, some characters are too thin to distinguish, and the number of images may not enough to tarin character set. So we preprocess the images with some mathematical morphology methods
* Mirror to invert image
* Interpolation to enlarge the image
* Dilation to make character easier to detect and separate
* Separation to recognition one line
* Rotation to get more training data

# 

## Mirror
Almost all given images to recognition is mirrored, we make symmetrical change in y-axis for each pixel. 
```
    y = img.shape[0]
    x = img.shape[1]
    img2 = copy.deepcopy(img)
    for i in range(x):
        for j in range(y):
            img2[j][i] = img[y - j - 1][i]
```

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
After that, we find the interpolated images are rough with a lot of edges and corners. To make edge smooth, we make a dilation operation after interpolation.
```
    kernel = np.ones((3,3))
    r = cv2.dilate(emptyImage, kernel)
```
## Separation

## Dilation
Dilation operation thicken the thin character, which is used in above preprocess. We think appropriately thicken the character is helpful for recognition.

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

