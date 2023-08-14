import cv2 as cv
import os 
from template import ROI
from template import Images
from matcher import match_Template


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))    # This is your Project Root

def display(str, img):
    cv.imshow(str, img)
    key = cv.waitKey(0)
    
    if (key == ord('q')):
        cv.destroyAllWindows()
        exit()

    if (key == ord('s')):
        print("XD")
        cv.imwrite('images/ss.jpg', img)


def seek_timer(frame):      # triggered only when found new milestone
    cropped = ROI.igt_timer.crop(frame)      
    templates = [image.template() for image in Images.numbers()]
    matches = match_Template(cropped, templates)


    for match in matches:   # sort by x and record time 
        num = match.template.value
        
        print(match.template.value)
        match.draw(cropped)

    display('timer', cropped)
    

def seek_achievement(frame):
    cropped = ROI.achievement.crop(frame)
    display('achievement', cropped)

    



# read latest vod 
path = '../vods/example.mp4'
vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("Video not found...")


while (True): 
    curr = vid.get(cv.CAP_PROP_POS_FRAMES)      # index of the frame to be read next
    total = vid.get(cv.CAP_PROP_FRAME_COUNT)
    ret, frame = vid.read()
    print(f'\rReading Frame: {int(curr)}/{int(total)}', end="")
    print('\n')
    if not ret:
        print("Finished reading video.")
        break
    
    seek_timer(frame)
    break
    


    
   
    
cv.destroyAllWindows()

