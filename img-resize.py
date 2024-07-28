import cv2

scale = 50
img = cv2.imread('charan.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('this is Qr code image', img)


img_z = img.size

print("image size is ", img.size)

