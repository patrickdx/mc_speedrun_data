import cv2 as cv
import numpy as np
from template import * 


def match_Template(img, temps: list[Template]) -> list[Match]:
    '''
    This function uses thresholding to match multiple templates at once. Templates may match more than once
    or incorrectly if threshold value is too low.
    '''

    matches = [] 

    for temp in temps:
        res = cv.matchTemplate(img, temp.img, cv.TM_CCOEFF_NORMED)
        locations = np.where(res >= temp.THRESHOLD)       # returns indexes of values over threshold (which means higher probability of match)

        if (locations[0].size == 0 and locations[1].size == 0):     # match not found
            continue

        else:  
            for pt in zip(locations[1], locations[0]):         # (rows, cols) swap them because we want (x,y) coords
                match = Match(pt, (pt[0] + temp.width, pt[1] + temp.height), temp)
                # print(match , "found.")
                matches.append(match)
                
    matches.sort(key = lambda x : x.pt1[0])         # sort by x position
    return matches 



def seek_achievements(frame, achievements : list[Template] , debug = False):
          
    adv_frame = ROI.achievement.crop(frame) 
    matches = match_Template(adv_frame, achievements)       # only expecting 1 match here 

    if len(matches) == 1:
        return matches[0].template
        # current_run.record(matched, seek_timer(frame)) 
    



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



        
# def filter_matches(res: np.ndarray, expected):
#     '''
#     Removes duplicate matches that are most certain of the same template, resulting from not having 
#     an adequate threshold value.
#     @expected: the expected number of matches of image
#     '''
#     threshold = 0.5
    
#     # or we can keep raising threshold until theres only expected amount of matches left
#     locations = np.where(res >= threshold)

#     while (locations[0].size > expected):       # this gets more and more selective
#         threshold += 0.03
#         locations = np.where(res >= threshold)
                  
#     print(f'found{locations[0].size} optimal matches')
#     return locations


    
