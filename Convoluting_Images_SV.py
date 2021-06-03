# Import necessary packages
import argparse
import numpy as np
import cv2
from skimage.exposure import rescale_intensity

ap = argparse.ArgumentParser()

# Image command line argument
ap.add_argument("-i", "--image", type = str, default = "Storm1.jpg")

# Created Kernel command line arguments
ap.add_argument("-tl", "--top_left", type = str, default = "1")
ap.add_argument("-tm", "--top_middle", type = str, default = "1")
ap.add_argument("-tr", "--top_right", type = str, default = "1")
ap.add_argument("-ml", "--middle_left", type = str, default = "1")
ap.add_argument("-mm", "--center", type = str, default = "-8")
ap.add_argument("-mr", "--middle_right", type = str, default = "1")
ap.add_argument("-bl", "--bottom_left", type = str, default = "1")
ap.add_argument("-bm", "--bottom_middle", type = str, default = "1")
ap.add_argument("-br", "--bottom_right", type = str, default = "1")

args = vars(ap.parse_args())

# Translating image command line argument into variable
image = cv2.imread(args["image"])

# Turning the image into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Converting created kernel command line arguments into variables
tl = int(args["top_left"])
tm = int(args["top_middle"])
tr = int(args["top_right"])
ml = int(args["middle_left"])
c = int(args["center"])
mr = int(args["middle_right"])
bl = int(args["bottom_left"])
bm = int(args["bottom_middle"])
br = int(args["bottom_right"])

# Function to apply kernels to image
def convolve(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	
  # Padding the border
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
	
	background = np.zeros((iH, iW), dtype="float32")
	
  # Computing new pixel values
	for x in range(pad, iW + pad):
		for y in range(pad, iH + pad):
			section = image[y - pad: y + pad + 1, x - pad: x + pad + 1]
			convolution = (section * kernel).sum()
			background[y - pad, x - pad] = convolution
	
  # Applying the kernel
	output = rescale_intensity(background, in_range=(0, 255))
	final = (output * 255).astype("uint8")
	
	return final

# Blurring
small = np.ones((7,7), dtype="float") * (1.0 / (7 * 7))
large = np.ones((21,21), dtype="float") * (1.0 / (21 * 21))

# Sharpen
sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype = "int")

# Laplacian- Detecting Edges
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype = "int")

# Created Kernel
created = np.array((
	[tl, tm, tr],
	[ml, c, mr],
	[bl, bm, br]), dtype = "int")

# Showing images with convolutional filters applied
cv2.imshow("Original", gray)
cv2.imshow("Small Blur", convolve(gray, small))
cv2.imshow("Large Blur", convolve(gray, large))
cv2.imshow("Sharpen", convolve(gray, sharpen))
cv2.imshow("Laplacian", convolve(gray, laplacian))
cv2.imshow("Created Filter", convolve(gray, created))
cv2.waitKey()

# This program was Convoluting_Images_SV_III.py by SarvasyaVikas
