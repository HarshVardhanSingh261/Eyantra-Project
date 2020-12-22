import task_1a_part1
import task_1b
import cv2


img=cv2.imread('img1.png')
cv2.imshow('image1',img)
cv2.waitKey(0)
wimg=task_1b.applyPerspectiveTransform(img)
cv2.imshow('image',wimg)
cv2.waitKey(0)
shapes=task_1a_part1.scan_image(img)
print(shapes)