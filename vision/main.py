import cv2 as cv
import os 
from template import * 
from matcher import match_Template
import spreadsheet
from run import logger
from run import Run 
import numpy as np 

def display(str, img, wait = False):
    cv.imshow(str, img)
    if (wait is True): key = cv.waitKey(0)      # frame by frame 
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
    print(len(matches))          # matches should be 7 in length
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



def seek_achievement(frame, achievement : Template) -> str:     # Checks if match was successful and matched expected amount of items.
    
    cropped = ROI.achievement.crop(frame)
    match = match_Template(cropped, [achievement])
    if len(match) == 1: return seek_timer(frame)
    return ""


def seek_achievements(frame, achievements : list[Template] , debug = False):
          
    adv_frame = ROI.achievement.crop(frame) 
    matches = match_Template(adv_frame, achievements)       # only expecting 1 match here for a frame 

    if len(matches) == 1:
        matched = matches[0].template
        current_run.record(matched, seek_timer(frame)) 
    



    # if debug is True:
    #     for match in matches:
    #         match.draw(cropped)
    #         display('achivement', cropped)


    # if len(matches) == 1:
    
    #     achievement = matches[0].template
    #     # things to do if match was successful
    #     display('achievement', cropped)
    #     Run.record(achievement, seek_timer(frame))    
    #     return True 


def seek_timer_freeze(frames: list) -> str:      # Returns true if timer is the same for all frames passed
    if len(frames) == 0: return False 

    # str = []
    # for frame in frames:
    #     str.append(seek_timer(frame))
    # print(str)

    # image comparison way 
    timers = [ROI.igt_timer.crop(frame) for frame in frames]
    result = all(np.array_equal(time, timers[0]) for time in timers)
    if result: 
        logger.info("frame feeze found")
        return seek_timer(frame[0])
    
    return ''


    # seek timer version 
    # res = seek_timer(frames[0])
    # for i in range(1, len(frames)):
    #     time = seek_timer(frames[i])
    #     if time == None or res != time: return False 

    

    # logger.info("frame freeze found")
    # # current_run.record(???, res)      TODO: record doesn't make sense since there is no template here... need to find abetter way to record and represent events in general
    # return True



def seek_pause() -> bool: 
    quit = ROI.quit_button.crop(frame)
    match = match_Template(quit, quitButtonTemplate)       # only expecting 1 match here for a frame 
    if len(match) == 1: return True 
    return False 


def seekReset(): 
    pass 


# 1. reset times, 2. record times 
def onReset():
    spreadsheet.save(current_run)
    current_run.clear()
     







cv.destroyAllWindows()


# ------------------- debugging methods ----------------------------

from package import VOD_DIR
from collections import deque       # fast pop for beginning elements 
from run import *

recent_frames = deque()
current_run = Run()
vid = cv.VideoCapture(VOD_DIR + 'full_run.mp4')
if not vid.isOpened(): raise FileNotFoundError("Video not found...")
vid.set(cv.CAP_PROP_POS_FRAMES, 10000)
ret, frame = vid.read()     # returns false if frame is unable to be read


while vid.isOpened():
    ret, frame = vid.read()
    logger.info(f'{int(vid.get(cv.CAP_PROP_POS_FRAMES))}/{int(vid.get(cv.CAP_PROP_FRAME_COUNT))}')


    # cache recent frames 
    recent_frames.append(frame) 
    if (len(recent_frames) > 5): recent_frames.popleft()
    

    display('video', frame, wait=True)            # show video
    # seek_timer(frame, debug=True)    # show timer 
    
    events = current_run.seek_next()
    # seek events method 
    for event in events:
        if event.getType() == EventType.TIMER_FREEZE and seek_pause() == False: timer = seek_timer_freeze(recent_frames)
        if event.getType() == EventType.TEMPLATE_MATCH: timer = seek_achievement(frame, [event], debug = True)     # need to test whether formulating all events first and then calling is better
        else: raise RuntimeError("This event is not recognized.")
        current_run.record(event, timer)


    if (len(recent_frames) == 5): seek_timer_freeze([frame for frame in recent_frames])

    
    #  event = current_run.seek_next() 
    # if (event.type == 'achivement') seek_acvhiements(event), some way find template off event.. 
    # if (event.type == 'timer_freeze') timer_freeze(event), current.run.record(event.name, time)
