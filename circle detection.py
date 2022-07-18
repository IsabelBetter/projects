import numpy as np
import cv2 as cv
src_img = cv.imread("REPLACE",0)
color_img = cv.cvtColor(src_img,cv.COLOR_GRAY2BGR)
circles_img = cv.HoughCircles(src_img,cv.HOUGH_GRADIENT,1.5,400,param1=200,param2=40,minRadius=0,maxRadius=0)
circles_img = np.uint16(np.around(circles_img))
for i in circles_img[0,:]:
    cv.circle(color_img,(i[0],i[1]),i[2],(0,255,0),2)
    cv.circle(color_img,(i[0],i[1]),2,(0,0,255),3)

cv.imshow('Original Image',src_img)
cv.imshow('Detected Circles',color_img)

cv.waitKey(0)
cv.destroyAllWindows()


#"C:\\Users\\max\\Downloads\\python\\circles.png" 