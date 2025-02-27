import cv2

image_1=cv2.imread("D:\python\Image_processing\Assignment_(26)/face.jpg")
image_2=cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)

for i,j in zip(range(0,180,1),range(180,0,-1)):
    image_2[i,j:j+80]=0
    if j==1:
        for x in range(79,-1,-1):
            i+=1
            image_2[i,0:j+x]=0

cv2.imshow("",image_2)
cv2.waitKey()
cv2.imwrite("Assignment_(26)/face.jpg",image_2)