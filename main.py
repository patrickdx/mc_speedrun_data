import cv2 as cv
import os 
from template import * 
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



def seek_achievement(frame, achievement : Template) -> bool:     # Checks if match was successful and matched expected amount of items.
    if adv_found(achievement): return False 
         
    cropped = ROI.achievement.crop(frame)
    template = achievement
    matches = match_Template(cropped, [template])
    assert len(matches) == 1, 'matched more than 1 achievment'
    
    if len(matches) == 1:
        achievement = matches[0].template.value

        # things to do if match was successful
        print(f'achivement{achievement}')
        display('achievement', cropped)
        match_sequence.append((achievement, seek_timer(frame)))     
        return True 
    
    return False


def seek_reset():   # if reset then go back to start
    pass 

def seek_timer_freeze(frames: list) -> bool:      # Returns true if timer is the same for all frames passed
    res = seek_timer(frames[0])
    for frame in frames:
        if res != seek_timer(frame): return False 

    return True

def adv_found(adv1 : Template) -> bool:       # checks if already found this achivement
    for adv, time in match_sequence:
        if adv == adv1.value: return True 

    return False
        


path = '../vods/example.mp4'
vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("Video not found...")

run_order = Images.run_order()      # the next achivement to 'look' for, since it has some linear ordering 
step = 0
ret, frame = vid.read()     # returns false if frame is unable to be read
match_sequence : list[tuple] = [] 


while ret: 

    curr, total = vid.get(cv.CAP_PROP_POS_FRAMES), vid.get(cv.CAP_PROP_FRAME_COUNT)
    spreadsheet.progress(curr, total, status = 'Reading Frame')
    # print(f'Looking for {chrono[next]}')


    next_adv = run_order[step]   

    if seek_achievement(next_adv): step += 1
    if next_adv == Images.FORTRESS or next_adv == Images.NETHER_EXIT: seek_achievement(Images.BASTION)

    if seek_reset(): match_sequence.clear()

    print(match_sequence)
    ret, frame = vid.read()     # should be last line

    
   
    
cv.destroyAllWindows()

