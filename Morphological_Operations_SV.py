# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line argument
ap.add_argument("-i", "--image", type=str, default = "X_F_Uniform.jpg")
args = vars(ap.parse_args())

# Translating command line argument into variable
image = cv2.imread(args["image"])
modified = image.copy()

# Erosion
for i in range(0, 4):
	eroded = cv2.erode(modified, None, iterations = i)
	cv2.imshow("Modified Image", eroded)
	cv2.waitKey(1000)

# Dilation
for i in range(0, 4):
	dilate = cv2.dilate(modified, None, iterations = i)
	cv2.imshow("Modified Image", dilate)
	cv2.waitKey(1000)

# Sizes that are being iterated over
sizes = [ (3, 3), (5, 5), (7, 7) ]

# Opening
for size in sizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
	opening = cv2.morphologyEx(modified, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Modified Image", opening)
	cv2.waitKey(1000)

# Closing
for size in sizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
	close = cv2.morphologyEx(modified, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Modified Image", close)
	cv2.waitKey(1000)

# Gradient
for size in sizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
	gradient = cv2.morphologyEx(modified, cv2.MORPH_GRADIENT, kernel)
	cv2.imshow("Modified Image", gradient)
	cv2.waitKey()

# Defining new kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

# Top Hat and Black Hat
blackhat = cv2.morphologyEx(modified, cv2.MORPH_BLACKHAT, kernel)
tophat = cv2.morphologyEx(modified, cv2.MORPH_TOPHAT, kernel)

# Displaying the images
cv2.imshow("Original", image)
cv2.imshow("Black Hat", blackhat)
cv2.imshow("Top Hat", tophat)
cv2.waitKey()

# This program was Morphological_Operations_SV_IX.py by SarvasyaVikas
