import os
import cv2


def show_img_jupyter(img):
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('image', image_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_img_jupyter_no_convert(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_img_OpenCV(img):    
    cv2.imshow('My Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop_img(img):
    
    # left, right
    x_l, x_r = 100,400 
    
    # up, down
    y_u, y_d = 0, 300 

    # crop image
    crop_img = img[y_u:y_d, x_l:x_r]  # notice: first y, then x
    
    return crop_img

def img_processing(img):
    img = crop_img(img)
    return img

file_name = "cat.jpg"

origin_img = cv2.imread(file_name)
show_img_jupyter(origin_img)
show_img_jupyter_no_convert(origin_img) # 未轉換顏色通道 BGR -> RGB
result_img = img_processing(origin_img)
show_img_jupyter(result_img)
cv2.imwrite('out.jpg', result_img)


