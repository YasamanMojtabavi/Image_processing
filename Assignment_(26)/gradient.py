import cv2
import numpy as np

my_image=np.zeros((255,255),dtype=np.uint8)

for i in range(0,255):
    my_image[i,0:255]=255-i

cv2.imwrite("Assignment_(26)/Image/gradient.jpg",my_image)
#cv2.imshow("",my_image)
#cv2.waitKey()