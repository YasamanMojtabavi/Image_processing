import cv2

image=cv2.imread("D:\python\Image_processing\Assignment_(26)/Image/rotate.jpg")

image_rotate=cv2.rotate(image,cv2.ROTATE_180)

cv2.imwrite("Assignment_(26)/Image/after_rotaate.jpg",image_rotate)