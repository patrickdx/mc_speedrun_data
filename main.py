import cv2 as cv
from vision.ROI import Frame



def display(str, img):
    cv.imshow(str, img)
    key = cv.waitKey(0)
    
    if (key == ord('q')):
        cv.destroyAllWindows()
        exit()

    if (key == ord('s')):
        print("XD")
        cv.imwrite('images/ss.jpg', img)


def seek_timer(frame):
    cropped = Frame.igt_timer.crop(frame)
    display('timer', cropped)

def seek_achievement(frame):
    cropped = Frame.achievement.crop(frame)
    display('achievement', cropped)

    



# read latest vod 
path = 'vods/example.mp4'
vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("Video not found...")

cv.imwrite('frame.png' ,vid.read()[1])

while (True): 
    curr = vid.get(cv.CAP_PROP_POS_FRAMES)      # index of the frame to be read next
    total = vid.get(cv.CAP_PROP_FRAME_COUNT)
    ret, frame = vid.read()
    
    if not ret:
        print("Finished reading video.")
        break
 
    


    
    print(f'\rReading Frame: {int(curr)}/{int(total)}', end="")
   
    
cv.destroyAllWindows()

