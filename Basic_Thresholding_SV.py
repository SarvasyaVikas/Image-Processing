# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")
ap.add_argument("-t", "--threshold", type=str, default = "150")

args = vars(ap.parse_args())

# Translating command line arguments into variables
image = cv2.imread(args["image"])
threshold = int(args["threshold"])

# Converting to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian blur to reduce high frequency noise
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# Deriving final images
(T, simple_binary) = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)
(T, simple_inv) = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY_INV)
(T, otsu_binary) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
(T, otsu_inv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Showing final images
cv2.imshow("Binary Simple Thresholding", simple_binary)
cv2.imshow("Binary Inverse Simple Thresholding", simple_inv)
cv2.imshow("Binary OTSU Thresholding", otsu_binary)
cv2.imshow("Binary Inverse OTSU Thresholding", otsu_inv)
cv2.waitKey()

# This program was Basic_Thresholding_SV_II.py by SarvasyaVikas
