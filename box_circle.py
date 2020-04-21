import argparse
import cv2
import numpy as np
# import imutils

canvas = np.zeros((300,300,3), dtype = "uint8")
red = (0,0,255)
var = 0
for i in range(0,canvas.shape[1],4):
    for j in range(0, canvas.shape[0] + 1):
        if j % 2 == var:
            cv2.rectangle(canvas, (j * 4, i), (4 * (j + 1), (i+1) * 4), red, -1)
        else:
            cv2.rectangle(canvas, (j * 4, i), (4 * (j + 1), (i+1) * 4), (0, 0, 0), -1)
    var = var + 1
    var = var % 2
green = (0,255,0)
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
cv2.circle(canvas, (centerX, centerY), 50, green, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)