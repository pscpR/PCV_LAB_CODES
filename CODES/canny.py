import cv2
import numpy as np

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

edges = cv2.Canny(blur, 100, 200)

result = cv2.hconcat([gray,edges])
cv2.imshow("Canny", result)
cv2.waitKey(0)