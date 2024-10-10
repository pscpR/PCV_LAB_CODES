import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(12,12))

plt.subplot(221)
plt.title("Original")
plt.imshow(gray)
plt.axis("off")

img_hist = cv2.calcHist([gray],[0],None,[256],[0,256])
plt.subplot(222)
plt.title("Grayscale")
plt.plot(img_hist)
plt.xlim([0,256])

plt.subplot(223)
plt.hist(gray.ravel(),256,[0,256])
plt.title("Using Ravel")

equalized = cv2.equalizeHist(gray)
plt.subplot(224)
plt.title("Hist Equalization")
plt.imshow(equalized,cmap='gray')
plt.axis("off")


plt.tight_layout()
plt.show()
