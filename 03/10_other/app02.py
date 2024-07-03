# import required libraries
import cv2

# load the input image
img = cv2.imread('convexhull.png')

# convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding to convert grayscale to binary image
ret,thresh = cv2.threshold(gray,100,255,0)

# find the contours
contours,hierarchy = cv2.findContours(thresh,
cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours detected:", len(contours))

# draw contour and shape number
for i, cnt in enumerate(contours):
   M = cv2.moments(cnt)
   x1, y1 = cnt[0,0]
   img1 = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
   cv2.putText(img, f'Contour:{i+1}', (x1, y1),
   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# compute shortest distance of point (350,250) from the contour
dist = cv2.pointPolygonTest(cnt,(350,250),True)
print(f'Shortest distance of Point (350,250) from contour{i+1}:', dist)
cv2.circle(img, (350,250), 4, (0, 0, 255), -1)
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()