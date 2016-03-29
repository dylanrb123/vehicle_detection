import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimuim area size")
args = vars(ap.parse_args())

if args.get('video', None) is None:
    # use the webcam
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)
else:
    # use the supplied file
    camera = cv2.VideoCapture(args['video'])

first_frame = None
