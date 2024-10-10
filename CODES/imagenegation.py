import cv2 

img = cv2.imread("image.jpg")
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
negative = cv2.bitwise_not(gray_scale)

cv2.imshow("Neg", negative)
key = cv2.waitKey(0)

if key == ord("s"):
    cv2.imwrite("negative.jpg", negative)