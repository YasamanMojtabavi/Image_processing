import cv2

my_image=cv2.imread("D:\python\image_processing\session(01)\images.jpg")
my_image_2=cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY)

#print(my_image_2)
print(my_image_2.shape)

cv2.imshow("alaki",my_image_2)


#my_image_2[10:17,18:199]=255

for i in range(0,10):
    for j in range(0,300):
        my_image_2[i,j]=255
my_image_2[0:168,0:10]=255
my_image_2[158:168,0:300]=255
my_image_2[0:168,290:300]=255
 

flower=my_image_2[10:168,25:100]
cv2.imshow("",flower)
cv2.waitKey()

my_image_2[10:168,225:300]=flower

cv2.imwrite("result.jpg",my_image_2)