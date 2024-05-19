import sys
import cv2

# 写真撮影
cc = cv2.VideoCapture(0)
rr, img = cc.read()
cv2.imwrite('pic.jpg', img)
cc.release()
