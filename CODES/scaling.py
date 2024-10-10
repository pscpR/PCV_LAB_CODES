import cv2

img = cv2.imread("image.jpg")

rows,cols = img.shape[:2]

img_shrinked = cv2.resize(img, (150,200), interpolation=cv2.INTER_AREA)

img_enlarged = cv2.resize(img_shrinked, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow("normal", img)
cv2.imshow("small", img_shrinked)
cv2.imshow("large", img_enlarged)
cv2.waitKey(0)

