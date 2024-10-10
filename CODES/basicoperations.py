import cv2
import numpy as np

img = cv2.imread("image.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

video_path = 'your_video_file.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("Reached the end of the video.")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
