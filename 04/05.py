from PIL import Image
import pytesseract
import numpy as np
import cv2

filename = '2_python-ocr.jpg'
img2 = np.array(Image.open(filename))
norm_img= np.zeros((img2.shape[0], img2.shape[1]))
img = cv2.normalize(img2, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
img = cv2.GaussianBlur(img, (1, 1), 0)
text = pytesseract.image_to_string(img)
print(text)
cv2.imwrite('ok.jpg', img) 
im = Image.open(r'ok.jpg')  
im.show()
