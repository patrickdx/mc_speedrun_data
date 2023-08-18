import cv2 as cv
import os 
from template import ROI
from template import Images
from matcher import match_Template
import spreadsheet

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
    
    if len(matches) > 0:    
        nums = []
        for match in matches: 
            nums.append(match.template.value)
            match.draw(cropped)

        mins = nums[0] + nums[1]
        secs = nums[2] + nums[3] 
        ms =   nums[4] + nums[5]
        display('timer', cropped)
        return '{mins}:{secs}:{ms}'
    
    # return mins*60 + secs + ms/1000



def seek_achievement(frame, achievement : Images) -> bool:     # Tries to match Images returns true if found / plays with the results 
    
    cropped = ROI.achievement.crop(frame)
    template = achievement.template()
    matches = match_Template(cropped, [template])
    assert len(matches) == 1, 'matched more than 1 achievment'

    if len(matches) == 1:
        achievement = matches[0].template.value

        # record achivement and time
        print(f'achivement{achievement}')
        display('achievement', cropped)
        global chrono
        chrono.remove(matches[0].template)
        return True 
    
    return False

def seek_reset():   # if reset then go back to start
    pass 


# read latest vod 
path = '../vods/example.mp4'
vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("Video not found...")

chrono = Images.achievements()      # list containingall the achivements 

ret, frame = vid.read()     # returns false if frame is unable to be read
next = 0

while ret: 
    curr = vid.get(cv.CAP_PROP_POS_FRAMES)      # index of the frame to be read next
    total = vid.get(cv.CAP_PROP_FRAME_COUNT)
    spreadsheet.progress(curr, total, status = 'Reading video')
    print('\n')
    print(f'Looking for {chrono[next]}')
    
    if seek_achievement(frame, chrono[next]):
        next += 1

    

    ret, frame = vid.read()

    
   
    
cv.destroyAllWindows()

