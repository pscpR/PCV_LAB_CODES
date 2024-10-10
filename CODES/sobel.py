import cv2
import numpy as np

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

edges = np.sqrt(sobelx**2 + sobely**2)
edges = np.uint8(np.absolute(edges))

_ , edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)

result = cv2.hconcat([gray,edges])
cv2.imshow("Result", result)
cv2.waitKey(0)