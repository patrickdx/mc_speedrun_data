import cv2 as cv
import numpy as np 

# img = cv.imread('./images/power-BI.jpg')   # default loaded in BGR format
# cv.imshow("window", img)
# print(type(img))
# if (cv.waitKey(1000) == ord('q')): print("XD")       # wait for x ms for user input before continuing, 0 is infinite

# print(img)

# video = cv.VideoCapture('./vods/1879662076.mp4')   # VideoCapture object to load in video

# while video.isOpened():
#     bool, frame = video.read()      # reads a frame (Matrix); returns true if successful
#     if (bool == False): 
#         print("could not read frame. video end?...")
#         break

#     print(video.get(cv.CAP_PROP_FRAME_HEIGHT))      # cap.get()/set() for properties of the video

#     cv.rectangle(frame, (0,0), (500,500), (255,0,0) ,3)

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)        # convert frame to grayscale
#     cv.imshow('window', gray)
#     print(gray)
#     if cv.waitKey(100000000) == ord('q'): break             # waitKey returns unicode value, compare with q for quit
#                                                     # lower value = speed up video, vice versa   


# video.release()
# cv.destroyAllWindows()


#--------------------------------------------------------------


img = np.zeros((300,512,3), np.uint8)               # 300 x 512 window with 3 channels
print(len(img[0]))
cv.imshow('window', img)
print(img.shape)
cv.waitKey(0)
