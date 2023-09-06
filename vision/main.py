import cv2 as cv
import os 
from template import * 
from matcher import match_Template
import spreadsheet
from run import logger
from run import run 


def display(str, img, wait = False):
    cv.imshow(str, img)
    if (wait is True): key = cv.waitKey(0)
    else: key = cv.waitKey(1)
    
    if key == ord('q'):
        cv.destroyAllWindows()
        exit()

    if key == ord('s'):  
        print("saving screenshot...")
        print(cv.imwrite('../images/screenshot.png', img))          # this only works if its in vision library btw 
        print(cv.error())



def seek_timer(frame, debug = False):      # triggered only when found new milestone
    TIMER_LENGTH = 7
    cropped = ROI.igt_timer.crop(frame)      
    
    templates = Image.numbers()
    matches = match_Template(cropped, templates)
    print(len(matches))
    nums = []
    for match in matches: 
        nums.append(match.template.value)
        match.draw(cropped)
        
    if debug is True: display('timer', cropped)
    if len(matches) == TIMER_LENGTH:
    
        nums = [str(num) for num in nums]
        mins = nums[0] + nums[1]
        secs = nums[2] + nums[3] 
        ms =   nums[4] + nums[5] + nums[6]
        return f'{mins}:{secs}:{ms}'
    
    # return mins*60 + secs + ms/1000



def seek_achievement(frame, achievement : list[Template], debug = False) -> bool:     # Checks if match was successful and matched expected amount of items.
    
    cropped = ROI.achievement.crop(frame)
    template = achievement
    matches = match_Template(cropped, [template])


    if debug is True:
        for match in matches:
            match.draw(cropped)
            display('achivement', cropped)


    if len(matches) == 1:
    
        achievement = matches[0].template
        # things to do if match was successful
        display('achievement', cropped)
        run.record(achievement, seek_timer(frame))    
        return True 
    
    return False


def seek_achievements(frame, achievements : list[Template] , debug = False):
          
    adv_frame = ROI.achievement.crop(frame) 
    matches = match_Template(adv_frame, achievements)       # only expecting 1 match here 

    if len(matches) == 1:
        matched = matches[0].template
        current_run.record(matched, seek_timer(frame)) 
    








def seek_reset():   # if reset then go back to start
    pass 

def seek_timer_freeze(frames: list) -> bool:      # Returns true if timer is the same for all frames passed
    res = seek_timer(frames[0])
    for frame in frames:
        if res != seek_timer(frame): return False 

    return True


   
    
cv.destroyAllWindows()


# ------------------- debugging methods ----------------------------

path = '../vods/full_run.mp4'

current_run = run()
vid = cv.VideoCapture(path)
if not vid.isOpened(): raise FileNotFoundError("Video not found...")
vid.set(cv.CAP_PROP_POS_FRAMES, 10000)
ret, frame = vid.read()     # returns false if frame is unable to be read

while vid.isOpened():
    frame1 = frame
    frame2 = frame1
    ret, frame = vid.read()
    logger.info(f'{int(vid.get(cv.CAP_PROP_POS_FRAMES))}/{int(vid.get(cv.CAP_PROP_FRAME_COUNT))}')

    display('video', frame)            # show video
    # seek_timer(frame, debug=True)    # show timer 
    # advs = current_run.seek_next()
    # seek_achievements(frame, advs, debug=True)
    print(seek_timer_freeze([frame1, frame, frame2]))

    


def show_timer():
    pass



