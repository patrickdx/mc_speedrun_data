import cv2 as cv
import os 
from template import * 
from matcher import match_Template
import spreadsheet



def display(str, img):
    cv.imshow(str, img)
    key = cv.waitKey(0)
    
    if (key == ord('q')):
        cv.destroyAllWindows()
        exit()

    if (key == ord('s')):  
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
        print(f'{mins}:{secs}:{ms}')
    
    # return mins*60 + secs + ms/1000



def seek_achievement(frame, achievement : Template, debug = False) -> bool:     # Checks if match was successful and matched expected amount of items.
         
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


def seek_reset():   # if reset then go back to start
    pass 

def seek_timer_freeze(frames: list) -> bool:      # Returns true if timer is the same for all frames passed
    res = seek_timer(frames[0])
    for frame in frames:
        if res != seek_timer(frame): return False 

    return True



def main():

    path = '../vods/full_run.mp4'
    vid = cv.VideoCapture(path)
    if not vid.isOpened(): raise FileNotFoundError("Video not found...")

    run_order = Image.run_order()      # the next achivement to 'look' for, since it has some linear ordering 
    step = 0
    ret, frame = vid.read()     # returns false if frame is unable to be read


    while ret: 

        curr, total = vid.get(cv.CAP_PROP_POS_FRAMES), vid.get(cv.CAP_PROP_FRAME_COUNT)
        # spreadsheet.progress(curr, total, status = 'Reading Frame')
        # print(f'Looking for {chrono[next]}')


        # next_adv = run_order[step]   

        # if seek_achievement(next_adv): step += 1
        # if next_adv == Images.FORTRESS or next_adv == Images.NETHER_EXIT: seek_achievement(Images.BASTION)

        # if seek_reset(): match_sequence.clear()

        seek_timer(frame, debug=True)
        ret, frame = vid.read()     # should be last line

        
   
    
cv.destroyAllWindows()


# ------------------- debugging methods ----------------------------
path = '../vods/full_run.mp4'
from run import run 
current_run = run()

def show_video():    
    vid = cv.VideoCapture(path)
    while vid.isOpened():
        ret, frame = vid.read()


        # display('video', frame)            # show video
        # seek_timer(frame, debug=True)    # show timer 
        next = current_run.next_achivement()
        seek_achievement(frame, next, debug=True)

        


def show_timer():
    pass



show_video()