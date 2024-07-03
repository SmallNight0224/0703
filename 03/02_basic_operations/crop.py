
import os

import cv2


img = "cat.jpg"
origin_img = cv2.imread(img)

print(origin_img.shape)

cropped_img = origin_img[90:170, 160:340]

cv2.imshow('img', origin_img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
