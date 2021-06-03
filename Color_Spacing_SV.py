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

# Denoted by title
cv2.imshow("RGB Image", image)

(b, g, r) = cv2.split(image)

zeros = np.zeros(image.shape[:2], dtype = "uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, r]))
cv2.imshow("Green", cv2.merge([zeros, g, zeros]))
cv2.imshow("Blue", cv2.merge([b, zeros, zeros]))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

(h, s, v) = cv2.split(hsv)

cv2.imshow("Hue", cv2.merge([h, zeros, zeros]))
cv2.imshow("Saturation", cv2.merge([zeros, s, zeros]))
cv2.imshow("Value", cv2.merge([zeros, zeros, v]))

lIaIbI = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

(lI, aI, bI) = cv2.split(lIaIbI)

cv2.imshow("L* Channel", cv2.merge([lI, zeros, zeros]))
cv2.imshow("A* Channel", cv2.merge([zeros, aI, zeros]))
cv2.imshow("B* Channel", cv2.merge([zeros, zeros, bI]))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray)

cv2.waitKey()

# This program was Color_Spacing_SV_II.py by SarvasyaVikas
