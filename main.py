import cv2 as cv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#reading image
image = cv.imread('/Users/payalsagwal/Documents/Docx/Vikas Docx/PHOTO.jpg')
# plt.imshow(image)
# plt.show()

#converting BGR image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# plt.imshow(gray_image)
# plt.show()

# image inversion
inverted_image = 255 - gray_image
# plt.imshow(inverted_image)
# plt.show()

blurred = cv.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv.divide(gray_image, inverted_blurred, scale=256.0)
# plt.imshow(pencil_sketch)
# plt.show()

cv.imshow("Original Image", image)
cv.imshow("gray Image", gray_image)
cv.imshow("inverted Image", inverted_image)
cv.imshow("Pencil Sketch of PHOTO", pencil_sketch)
cv.waitKey(0)

