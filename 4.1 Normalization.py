import cv2
path = '/home/mhovhannisyan/Desktop/SJSU/270: DATA PROCESS/test-20230417T025203Z-001/test/combined/14.png'

# read the input image as grayscale image
img = cv2.imread(path,0)
print("Image data before Normalize:\n", img)

# Apply threshold to create a binary image
ret,thresh = cv2.threshold(img,140,255,cv2.THRESH_BINARY)
print("Image data after Thresholding:\n", thresh)

# normalize the binary image
img_normalized = cv2.normalize(thresh, None, 0, 1.0,
cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# visualize the normalized image
cv2.imshow('Normalized Image', img_normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image data after Normalize:\n", img_normalized)