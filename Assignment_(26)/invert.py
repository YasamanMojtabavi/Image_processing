import cv2

image_1=cv2.imread("D:\python\Image_processing\Assignment_(26)/1.jpg")
image_2=cv2.imread("D:\python\Image_processing\Assignment_(26)/2.jpg")

image_11=255-image_1 
image_22=255-image_2

cv2.imwrite("Assignment_(26)/invert_2.jpg",image_22)
cv2.imwrite("Assignment_(26)/invert_1.jpg",image_11)
