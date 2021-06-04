# Import necessary packages
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "X/Rogue.jpg")
ap.add_argument("-c", "--connectivity", type=int, default = 4)
ap.add_argument("-hI", "--has_I", type=str, default = 0)
ap.add_argument("-hL", "--has_L", type=str, default = 0)

args = vars(ap.parse_args())

# Converting command line argument to variable
image = cv2.imread(args["image"])

# Resizing image
resize = cv2.resize(image, (745, 960))

# Converting to grayscale and binary
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)[1]

# Getting rid of high frequency noise
dilated = cv2.dilate(thresh, None, iterations = 3)
eroded = cv2.erode(dilated, None, iterations = 3)

# Collecting components
components = cv2.connectedComponentsWithStats(eroded, args["connectivity"], cv2.CV_32S)
(numLabels, labels, stats, centroid) = components

# Creating final image
mask = np.zeros(gray.shape, dtype = "uint8")

# Functions for special cases
has_I = int(args["has_I"])
has_L = int(args["has_L"])

def is_I(h, w, area):
	if h < 30 and h > 15 and w < 4 and area > 40 and area < 120:
		return True
	else:
		return False

def is_L(h, w, area):
	if h < 30 and h > 15 and w > 20 and area > 80 and area < 120:
		return True
	else:
		return False

# Loop to filter out distractor components
for i in range(1, numLabels):
	x = stats[i, cv2.CC_STAT_LEFT]
	y = stats[i, cv2.CC_STAT_TOP]
	w = stats[i, cv2.CC_STAT_WIDTH]
	h = stats[i, cv2.CC_STAT_HEIGHT]
	area = stats[i, cv2.CC_STAT_AREA]
	
  # Conditions for being a component
	keepWidth = w > 1 and w < 40
	keepHeight = h > 15 and h < 40
	keepArea = area > 110 and area < 300
	
  # Get rid of solid components
  dim = h + w
	is_hollow = dim > 44

  # Apply components to mask
	if all((keepWidth, keepHeight, keepArea, is_hollow)):
		componentMask = (labels == i).astype("uint8") * 255
		mask = cv2.bitwise_or(mask, componentMask)
		print(w, h, area)
  
  # Loops for special cases
	if has_I == 0:	
		if is_I(h, w, area) == True:
			componentMask = (labels == i).astype("uint8") * 255
			mask = cv2.bitwise_or(mask, componentMask)
			print(w, h, area)
	if has_L == 0:
		if is_L(h, w, area) == True:
			componentMask = (labels == i).astype("uint8") * 255
			mask = cv2.bitwise_or(mask, componentMask)
			print(w, h, area)

# Show steps from the process
cv2.imshow("Original", image)
cv2.imshow("Resize", resize)
cv2.imshow("Grayscale", gray)
cv2.imshow("Binary", thresh)
cv2.imshow("Dilate", dilated)
cv2.imshow("Erode", eroded)
cv2.imshow("Components", mask)
cv2.waitKey()

# This program was Connected_Components_SV_XV.py by SarvasyaVikas
