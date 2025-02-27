import cv2

my_image=cv2.imread("D:\python\image_processing\session(02)\images.jpg")
my_image=cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY)

threshold=100
my_image[my_image>threshold]=255
my_image[my_image<=threshold]=0

cv2.rectangle(my_image,(30,35),(350,410),128,4)

cv2.imshow("chess board",my_image)
cv2.waitKey()
