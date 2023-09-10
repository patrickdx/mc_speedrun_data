import cv2 as cv
import numpy as np
from numpy import ndarray as Mat

class Video:
    def __init__(self, path):
        self.video = cv.VideoCapture(path)
        if not self.video.isOpened(): raise FileNotFoundError("video not found")
        
        self.frames = self.video.get(cv.CAP_PROP_FRAME_COUNT)
        self.cur_frame = 0

        self.displayInfo()
    

    def read(self) -> Mat:
            # 0-based index of the frame to be decoded/captured next.
            nextFrame = self.video.get(cv.CAP_PROP_POS_FRAMES)
            print(f'reading frame {nextFrame}')        

            ret, frame = self.video.read()
            assert ret is True and frame is not None, 'cant read frame'
            self.cur_frame += 1
            return frame


    def seek(self, frame_no):
        assert frame_no < self.frames, 'invalid frame number'
        self.video.set(cv.CAP_PROP_POS_FRAMES, frame_no)


    def _displayInfo(self):
        fps = self.video.get(cv.CAP_PROP_FPS)
        print(f'Reading video with {self.frames} frames with frame rate {fps}') 
