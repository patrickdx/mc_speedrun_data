from Video import Video
from Milestone import Milestone
import matcher
import cv2 as cv


# read latest vod 
path = 'the_latest_vod.mp4'

vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("video not found") # idk if this is sufficient enough

while (cv.CAP_PROP_POS_FRAMES <= cv.CAP_PROP_FRAME_COUNT):
    frame = vid.read()

    # try to match the frame continuing sequentially 
    matcher.match_Template()
