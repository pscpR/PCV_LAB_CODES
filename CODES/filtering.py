import cv2
import numpy as np

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.float32) / 25

mean_filter = cv2.filter2D(gray,-1,kernel)

median_filter = cv2.medianBlur(gray,5)

sharpening = cv2.Laplacian(gray, cv2.CV_64F)
sharpening = cv2.convertScaleAbs(sharpening)

result = cv2.hconcat([gray,mean_filter,median_filter,sharpening])
cv2.imshow("Result",result)
cv2.waitKey(0)
