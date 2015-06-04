import cv2
import numpy as np
import pdb
from matplotlib import pyplot as plt

img = cv2.imread('sampleFaceImage.png',0)

img = cv2.GaussianBlur(img,(5,5),0)
#kernel = np.ones((5,5),np.float32)/25
#img = cv2.filter2D(img,-1,kernel)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelx = sobelx/(sobelx.max())
laplacian = laplacian/laplacian.max()
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobely = sobely/sobely.max()

sobel = (sobelx+sobely)/2;


erode_kernel = np.ones((5,5),np.uint8)
img2 = cv2.erode(sobel,erode_kernel,iterations = 1)
cv2.imshow('eroded image',img2)

img3 = cv2.dilate(laplacian,erode_kernel,iterations = 1)
cv2.imshow('dilated image',img3)
cv2.waitKey(0)

# plt.subplot(2,1,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,1,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('laplacian'), plt.xticks([]), plt.yticks([])

# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

cv2.imshow('laplacian',laplacian/laplacian.max())
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('sobel', sobel/sobel.max())
cv2.waitKey(0)

cv2.destroyAllWindows()
pdb.set_trace();
#plt.show()