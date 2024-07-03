import os
import cv2


file_name = "cat.jpg"
origin_img = cv2.imread(file_name)
cv2.imwrite('out.jpg', origin_img)
cv2.imshow('image', origin_img)
cv2.waitKey(0)
