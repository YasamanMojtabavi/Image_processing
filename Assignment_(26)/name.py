import cv2
import numpy as np

my_image=np.zeros((180,180),dtype=np.uint8)

my_image[0:180,0:180]=255
coy_image=my_image[80:90,80:90] -255

for i,j in zip(range(130,40,-10),range(40,130,10)):
    my_image[j:j+10,i:i+10]=coy_image

for i in range(40,80,10):
    my_image[i:i+10,i+10:i+20]=coy_image

    



cv2.imshow("",my_image)
cv2.waitKey()
cv2.imwrite("Assignment_(26)/Image/name.jpg",my_image)
