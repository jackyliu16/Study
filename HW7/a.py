import cv2

img_o = cv2.imread("OIP-C.jpg")
b, g, r = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow('green', g)
cv2.imshow("red", r)