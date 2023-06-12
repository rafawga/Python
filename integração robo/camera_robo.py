# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:59:59 2022

@author: Rafawga
"""


import numpy as np
import argparse
import imutils
import cv2
from pyfirmata import Arduino,util
import time

# board = Arduino("COM3")


def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())
blackLower = (9, 30, 30)
blackUpper = (25, 170, 255)
if not args.get("video", False):
	camera = cv2.VideoCapture(1)
else:
	camera = cv2.VideoCapture(args["video"])
while True:
    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
    	break
    frame = imutils.resize(frame, width=600)
    frame = frame[35:330, 235:385]
    frame = zoom(frame)
    
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.line(frame, (150, 0), (150, 600), (0,0,0), 1)
    cv2.line(frame, (0, 155), (600, 155), (0,0,0), 1)
    cv2.line(frame, (0, 305), (600, 305), (0,0,0), 1)
    cv2.line(frame, (0, 455), (600, 455), (0,0,0), 1)
    maskBlack = cv2.inRange(hsv, blackLower, blackUpper)
    maskBlack = cv2.erode(maskBlack, None, iterations=2)
    maskBlack = cv2.dilate(maskBlack, None, iterations=2)
    cntBlack = cv2.findContours(maskBlack.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    centerBlack = None

    
    if len(cntBlack) > 0:
        cBlack = max(cntBlack, key=cv2.contourArea)
        rectBlack = cv2.minAreaRect(cBlack)
        cv2.circle(frame,(int(rectBlack[0][0]), int(rectBlack[0][1])), 5, (0,255,239),-1)
        mX = int(rectBlack[0][0])
        mY = int(rectBlack[0][1]) 
        print("Mx:",mX)
        print("My",mY)
        
        if mX < 150:
            if mY < 155:
                a = 6
            elif mY < 305:
                a = 7
            elif mY < 455:
                a = 8
            elif mY > 455:
                a = 9
        elif mX > 150:
            if mY < 155:
                a = 2
            elif mY < 305:
                a = 3
            elif mY < 455:
                a = 4
            elif mY > 455:
                a = 5
    
        print(a)
        boxBlack = cv2.boxPoints(rectBlack)
        boxBlack = np.int0(boxBlack)
        MBlack = cv2.moments(cBlack)
        centerBlack = (int(MBlack["m10"] / MBlack["m00"]), int(MBlack["m01"] / MBlack["m00"]))
        cv2.drawContours(frame, [boxBlack], 0, (79,79,79), 2)   '   '
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
    	break
camera.release()
cv2.destroyAllWindows()
