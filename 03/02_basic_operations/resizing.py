
import os

import cv2


img = "cat.jpg"
origin_img = cv2.imread(img)

resized_img = cv2.resize(origin_img, (300, 200))

print(origin_img.shape)
print(resized_img.shape)

cv2.imshow('img', origin_img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)

