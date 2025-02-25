import cv2
import numpy as np
global image_3

####################################################################################
def find_difference(image_1,image_2,x,z):
    global image_3

    if z==1:
        #+image_1=cv2.medianBlur(image_1,5)
        image_2=cv2.medianBlur(image_2,5)
        result=image_2 - image_1
        result=cv2.medianBlur(result,5)
    if z==0:
        result=image_2 - image_1

   

    conturs,_=cv2.findContours(result,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 


    for contur in conturs:
        if cv2.contourArea(contur)>x:
            x,y,w,h=cv2.boundingRect(contur)
            cv2.rectangle(result,(x,y),(x+w,y+h),(255,255,255),3)
            cv2.rectangle(image_3,(x,y),(x+w,y+h),(80,80,255),3)

    result=255-result
    #cv2.imwrite("result.jpg",result)
    #cv2.imshow("اصلی",result)
    #cv2.waitKey()
    cv2.imshow("resullt",image_3)
    cv2.waitKey()
####################################################################################
def rotation_angle(image_1,image_2):

   
    orb = cv2.ORB_create()
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2, None)

    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors_1, descriptors_2)

    #matches = sorted(matches, key=lambda x: x.distance)

    if len(matches) > 10:
        src_pts = np.float32([keypoints_1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)


        M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        
        angle_rad = np.arctan2(M[1, 0], M[0, 0])
        angle_deg = np.degrees(angle_rad)

        return 0,angle_deg
    else:
        return 1,0


####################################################################################
def matching(image_2,angle):
    

    h, w = image_2.shape[:2]
    center = (w // 2, h // 2)  
    rotation_matrix = cv2.getRotationMatrix2D(center, -angle, 1.0) 
    image_2 = cv2.warpAffine(image_2, rotation_matrix, (w, h))

    #cv2.imshow("1",image_1)
    #cv2.waitKey()
    #cv2.imshow("2",image_2)
    #cv2.waitKey()
    return image_2
####################################################################################  
def menu():
    global image_3
  

    choice_1=""
    choice_2=""
    x=0
    z=0
    l=127

    while(choice_1!="end" and choice_2!="end"):
        choice_1=input("Hello,please choose  photo1 from this number(11,22,30,40,50,60,70): ")
        choice_2=input("and chooise photo_2(10,21/20,31,41,51,61,71/72): ")

        if choice_1=="11" or choice_1=="30" or choice_1=="40" or choice_1=="60" or choice_1=="70":
            x=250
       
        elif choice_1=="50":
            x=150
            
           
        elif choice_1=="22"or choice_2=="72":
            l=210
            x=980
            z=1
        
            
        return 1,str(choice_1),str(choice_2),x,z,l
    
    return 0,0,0
    

####################################################################################
def main():
    global image_3
    
    chek,choice_1,choice_2,x,z,l=menu()
    
    
    if chek==1:
        image_1=cv2.imread("D:\python\_Python\project/"+str(choice_1) +".jpg")
        image_2=cv2.imread("D:\python\_Python\project/"+str(choice_2) +".jpg")
        image_3=image_1
        image_1=cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
        image_2=cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)
                
        _,image_1 =cv2.threshold(image_1,l,255,cv2.THRESH_BINARY)       
        _,image_2 =cv2.threshold(image_2,l,255,cv2.THRESH_BINARY)

        rows_1,col_1=image_1.shape
        image_2 = cv2.resize(image_2, ( col_1,rows_1))

        switch,angle=rotation_angle(image_1,image_2)
        if switch==1:
            print("2 images are not the same")
        if switch==0:
            angle_s=str(angle)
            print("Image_2 is rotated "+ angle_s +" degrees.")
            if abs(angle)>30:
                image_2=matching(image_2,angle)
                #cv2.imshow("1",image_1)
                #cv2.waitKey()
                #cv2.imshow("22",image_2)
                #cv2.waitKey()
                find_difference(image_1,image_2,x,z)

            else:
                find_difference(image_1,image_2,x,z)

    else:
        print("end.")

main()