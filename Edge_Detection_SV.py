# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")
ap.add_argument("-l", "--lower", type=str, default = "90")
ap.add_argument("-u", "--upper", type=str, default = "180")

args = vars(ap.parse_args())

# Translating command line arguments into variables
image = cv2.imread(args["image"])

# Limits for Canny edge detector
lower = int(args["lower"])
upper = int(args["upper"])

# Converting the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blurring the image
blurred = cv2.bilateralFilter(gray, 9, 30, 9)

# Detecting edges with Canny edge detector & displaying result
edges_detected = cv2.Canny(blurred, 90, 180)
cv2.imshow("Detected Edges", edges_detected)
cv2.waitKey()

# This program was Edge_Detection_SV_I.py by SarvasyaVikas
