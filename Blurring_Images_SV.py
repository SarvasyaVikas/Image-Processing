# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line argument
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")

args = vars(ap.parse_args())

# Translating command line argument into variable
image = cv2.imread(args["image"])

X = 1
Y = 1

# Gaussian blurring
while X < 50 and Y < 50:
	Gaussian = cv2.GaussianBlur(image, (X, Y), 0)
	cv2.imshow("Gaussian Blur", Gaussian)
	cv2.waitKey(100)
	X += 2
	Y += 2
	
X = 49
Y = 49

while X > 0 and Y > 0:
	Gaussian = cv2.GaussianBlur(image, (X, Y), 0)
	cv2.imshow("Gaussian Blur", Gaussian)
	cv2.waitKey(100)
	X -= 2
	Y -= 2

# Bilateral filtering
def bilateral(image, diameter, sigmaColor, sigmaSpace):
	bilateral = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
	return bilateral

# Infinite loop
while True:
	sigmaColor = 0
	while sigmaColor < 100:
		cv2.imshow("Bilateral Filter", bilateral(image, 15, 50, 30))
		cv2.waitKey(100)
		sigmaColor += 1
    
# This program was Blurring_Images_SV_XI.py by SarvasyaVikas
