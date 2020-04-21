from __future__ import print_function
import argparse
import cv2
import numpy.core.multiarray

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

print(image.shape)

# cv2.imshow("Image", image)


(b,g,r) = image[0,0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# cv2.waitKey(0)
# cv2.imwrite("newImage.jpg", image)

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0,255,0)
print(image[219, 90])
cv2.imshow("Updated", image)
cv2.waitKey(0)






