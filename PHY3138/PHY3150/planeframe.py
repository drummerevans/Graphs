# USAGE
# python planeframe.py
# python planeframe.py --video movie.mp4 --left left.dat --right right.dat --outputvideo outputvideo.mp4

# import the necessary packages
import numpy as np
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

# initialise frame counter
framecount = 0


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
	help="path to input video file")
ap.add_argument("-o", "--outputvideo", type=str,
        help="path to output video file")
ap.add_argument("-l", "--left", type=str,
        help="path to left tracking coords")
ap.add_argument("-r", "--right", type=str,
        help="path to right tracking coords")
ap.add_argument("-c", "--centre", type=str,
        help="path to centre tracking coords")
args = vars(ap.parse_args())

# set up output file
fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
out = cv2.VideoWriter(args["outputvideo"], fourcc, 10.0, (854,480))

# get tracking data
indata = np.loadtxt(args["left"],delimiter=' ')
lframein,x1,w,y1,h = indata.T
lframeindex = lframein.astype(np.int)
lminindex = np.min(lframeindex)
x1 = x1+w/2
y1 = y1+h/2
indata = np.loadtxt(args["right"],delimiter=' ')
rframein,x2,w,y2,h = indata.T
rframeindex = rframein.astype(np.int)
rminindex = np.min(rframeindex)
x2 = x2+w/2
y2 = y2+h/2
minindex = np.maximum(lminindex,rminindex)
loff = minindex - lminindex
roff = minindex - rminindex

# extract the OpenCV version info
(major, minor) = cv2.__version__.split(".")[:2]


# if a video path was not supplied, grab the reference to the web cam
if not args.get("video", False):
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(1.0)

# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])


# loop over frames from the video stream
while True:
	# grab the current frame, then handle if we are using a
	# VideoStream or VideoCapture object
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
        
	framecount = framecount+1

	# check to see if we have reached the end of the stream
	if frame is None:
		break

	# resize the frame (so we can process it faster) and grab the
	# frame dimensions
	frame = imutils.resize(frame, width=1000)
	(H, W) = frame.shape[:2]

	fc = framecount-minindex
	fc1 = fc + loff
	fc2 = fc + roff
	if framecount >= minindex and fc1<len(x1) and fc2<len(x2):
		framehalfsizex = 1.2*np.sqrt((x1[fc1]-x2[fc2])*(x1[fc1]-x2[fc2])+(y1[fc1]-y2[fc2])*(y1[fc1]-y2[fc2]))/2.0
		framecx = (x1[fc1]+x2[fc2])/2.0
		framecy = (y1[fc1]+y2[fc2])/2.0
#                framecx = xc[fc]
#                framecy = yc[fc]
		minx = (framecx-framehalfsizex).astype(np.int)
		maxx = (framecx+framehalfsizex).astype(np.int)
		framehalfsizey = framehalfsizex*480.0/854.0
		miny = (framecy-framehalfsizey).astype(np.int)
		maxy = (framecy+framehalfsizey).astype(np.int)
		framegrab = frame[miny:maxy, minx:maxx]
		frameout = cv2.resize(framegrab,(854,480)).astype(np.uint8)
		cv2.line(frameout,(0,240),(853,240),(255,255,255),1)
		cv2.line(frameout,(427,0),(427,479),(255,255,255),1)
		out.write(frameout)
	# show the output frame
#	cv2.imshow("Frame", frame)
#	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
#	elif key == ord("q"):
#		break

# if we are using a webcam, release the pointer
if not args.get("video", False):
	vs.stop()

# otherwise, release the file pointer
else:
	vs.release()

# close all windows
cv2.destroyAllWindows()
