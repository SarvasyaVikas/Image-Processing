# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line argument
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")

args = vars(ap.parse_args())

# Translating command line argument into variable
image = cv2.imread(args["image"])

# Converting image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blur to reduce high frequency noise
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Adaptive thresholding
final = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Adaptive Thresholded Image", final)
cv2.waitKey()

# Function to clean image
def reduce_noise(image, arr_size):
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (arr_size, arr_size) )
	opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
	return opening

# Applying cleaning function
size = 1
while size < 4:
	cv2.imshow("Processed Image", reduce_noise(final, size))
	cv2.waitKey()
	size += 2
  
# This program was Adaptive_Thresholding_SV_I.py by SarvasyaVikas
