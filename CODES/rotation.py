import cv2

img  = cv2.imread("image.jpg")

angle = 45
h,w = img.shape[:2]

M = cv2.getRotationMatrix2D((w/2 , h/2), angle, 1)
rotated_img = cv2.warpAffine(img, M, (w,h))

result = cv2.vconcat([img,rotated_img])
cv2.imshow("Rotation", result)
cv2.waitKey(0)