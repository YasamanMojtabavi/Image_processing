import cv2
import numpy as np

my_image_2=np.zeros((80,80),dtype=np.uint8)

for i in range(0,80,10):
    for j  in range(0,80,10):
        if ((i+j)%20)!=0 :
            my_image_2[i:i+10,j:j+10]=0
        else:
            my_image_2[i:i+10,j:j+10]=255
            
cv2.imwrite("Assignment_(26)/chess board.jpg",my_image_2)
