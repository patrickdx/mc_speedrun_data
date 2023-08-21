import cv2 as cv
import os 
from template import ROI
from template import Images
from matcher import match_Template
import spreadsheet
from collections import deque  # fast appends and pops from both ends. For example:


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
    TIMER_LENGTH = 7
    cropped = ROI.igt_timer.crop(frame)      
    
    templates = Images.numbers()
    matches = match_Template(cropped, templates)
    
    if len(matches) == TIMER_LENGTH:    
        nums = []
        for match in matches: 
            nums.append(match.template.value)
            match.draw(cropped)
        

        nums = [str(num) for num in nums]
        mins = nums[0] + nums[1]
        secs = nums[2] + nums[3] 
        ms =   nums[4] + nums[5] + nums[6]
        display('timer', cropped)
        return f'{mins}:{secs}:{ms}'
    
    else: print("timer not read properly...")
    
    # return mins*60 + secs + ms/1000



def seek_achievement(frame, achievement : Images) -> bool:     # Checks if match was successful and matched expected amount of items.
    
    cropped = ROI.achievement.crop(frame)
    template = achievement
    matches = match_Template(cropped, [template])
    assert len(matches) == 1, 'matched more than 1 achievment'
    
    if len(matches) == 1:
        achievement = matches[0].template.value

        # record achivement and time
        print(f'achivement{achievement}')
        display('achievement', cropped)
        return True 
    
    return False

def seek_reset():   # if reset then go back to start
    pass 


# read latest vod 
path = '../vods/example.mp4'
vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("Video not found...")

run_order = deque(Images.run_order())      # nether -> bastion/fort -> stronghold
ret, frame = vid.read()     # returns false if frame is unable to be read
next = 0

while ret: 
    curr, total = vid.get(cv.CAP_PROP_POS_FRAMES), vid.get(cv.CAP_PROP_FRAME_COUNT)
    
    spreadsheet.progress(curr, total, status = 'Reading Frame')
    # print(f'Looking for {chrono[next]}')
    

    if isinstance(run_order[0] , tuple):
        for i in run_order[0]:
            if seek_achievement(i): run_order.remove(i)

    # try to look for ahivement, if so then look timer
    if seek_achievement(frame, run_order[0]):
        run_order.popleft()
        # seek_timer(frame)



    ret, frame = vid.read()     # should be last line

    
   
    
cv.destroyAllWindows()

