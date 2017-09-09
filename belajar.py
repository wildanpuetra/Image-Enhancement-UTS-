import cv2

image = cv2.imread('D:\Pictures\IMG_20170303_080827.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Lawu.jpg', gray)
