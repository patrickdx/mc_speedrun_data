import cv2 as cv

# img = cv.imread('./images/power-BI.jpg')   # default loaded in BGR format
# cv.imshow("window", img)
# print(type(img))
# if (cv.waitKey(1000) == ord('q')): print("XD")       # wait for x ms for user input before continuing, 0 is infinite

# print(img)

video = cv.VideoCapture('./vods/1879662076.mp4')   # VideoCapture object to load in video

while video.isOpened():
    bool, frame = video.read()      # reads a frame; returns true if successful
    if (bool == False): 
        print("could not read frame. video end?...")
        break

    print(video.get(cv.CAP_PROP_FRAME_HEIGHT))      # cap.get()/set() for properties of the video
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)        # convert frame to grayscale
    cv.imshow('window', gray)
    if cv.waitKey(1) == ord('q'): break             # waitKey returns unicode value, compare with q for quit
                                                    # lower value = speed up video, vice versa   


video.release()
cv.destroyAllWindows()


