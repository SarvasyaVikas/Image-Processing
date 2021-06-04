# Import necessary packages
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()

# Command line argument
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")

args = vars(ap.parse_args())

# Translating command line argument into variable
image = cv2.imread(args["image"])

# Automatic Edge Detector function
def auto_canny(image, sigma):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edge_detected = cv2.Canny(image, lower, upper)
	return edge_detected

# Conversion to grayscale and bilateral filter
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.bilateralFilter(gray, 9, 25, 11)

# Displaying the derived image
cv2.imshow("Automatic Edge Detection", auto_canny(blurred, 0.33))
cv2.waitKey()

# This program was Automatic_Detection_SV_0.py by SarvasyaVikas
