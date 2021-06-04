# Import necessary packages
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")
ap.add_argument("-f", "--function", type=str, default = "0")

args = vars(ap.parse_args())

# Translating command line arguments into variables
image = cv2.imread(args["image"])
function = int(args["function"])

# Converting image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function #0 : Deriving Sobel & Scharr Convolutions from the Image
if function == 0:
	gX_So = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = 3)
	gY_So = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = 3)

	gX_Sch = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
	gY_Sch = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

	gX_So = cv2.convertScaleAbs(gX_So)
	gY_So = cv2.convertScaleAbs(gY_So)

	gX_Sch = cv2.convertScaleAbs(gX_Sch)
	gY_Sch = cv2.convertScaleAbs(gY_Sch)

	combined_So = cv2.addWeighted(gX_So, 0.5, gY_So, 0.5, 0)
	combined_Sch = cv2.addWeighted(gX_Sch, 0.5, gY_Sch, 0.5, 0)

	cv2.imshow("Sobel X", gX_So)
	cv2.imshow("Sobel Y", gY_So)
	cv2.imshow("Sobel Combined", combined_So)
	cv2.imshow("Scharr X", gX_Sch)
	cv2.imshow("Scharr Y", gY_Sch)
	cv2.imshow("Scharr Combined", combined_Sch)
	cv2.waitKey()

# Function #1 : Deriving gradient magnitude & orientation from the image
if function == 1:
	gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
	gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

	magnitude = np.sqrt((gX ** 2) + (gY ** 2))
	orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

	(fig, axs) = plt.subplots(nrows = 1, ncols = 3, figsize = (8, 4))

	axs[0].imshow(gray, cmap = "gray")
	axs[1].imshow(magnitude, cmap = "jet")
	axs[2].imshow(orientation, cmap = "jet")

	axs[0].set_title("Grayscale")
	axs[1].set_title("Gradient Magnitude")
	axs[2].set_title("Gradient Orientation")

	for i in range(0, 3):
		axs[i].get_xaxis().set_ticks([])
		axs[i].get_yaxis().set_ticks([])

	plt.tight_layout()
	plt.show()
  
  # This program was Imaging_Gradients_SV_II.py by SarvasyaVikas
