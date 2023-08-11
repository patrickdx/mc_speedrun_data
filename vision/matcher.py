import cv2 as cv
import numpy as np
from match import Template, Match, display


def match_single(img, temp: Template) -> Match:
    res = cv.matchTemplate(img, temp.img, cv.TM_CCOEFF_NORMED)   # output image (W-w+1, H-h+1)       243 x 238
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    top_left = max_loc   # (x,y)
    bottom_right = (max_loc[0] + temp.width, max_loc[1] + temp.height)    

    # If match:
    match = Match(top_left, bottom_right, temp)
    img1 = img.copy()
    match.drawRect(img1)
    display(str, img1)
    return match 

    # Else:
    return None
def match_Template(img, temps: list[Template]) -> list[Match]:
    '''
    This function uses thresholding to match multiple templates at once. Templates may match more than once
    or incorrectly if threshold value is too low.
    '''
    matches = [] 

    for temp in temps:
        res = cv.matchTemplate(img, temp, cv.TM_CCOEFF_NORMED)
        locations = np.where(res >= temp.THRESHOLD)       # returns indexes of over threshold (which means higher probability of match)

        if (locations[0].size == 0 and locations[1].size == 0):
            print("matches for current template could not be found. continuing...")

        else:  
            for pt in zip(locations[1], locations[0]):         # (rows, cols) swap them because we want (x,y) coords
                print(pt)
                matches.append(Match(pt[0] + temp.width, pt[1] + temp.height, temp))

            
        return matches
        



    
