import cv2 as cv
import numpy as np
from template import Template, Match


def match_single(img, temp: Template) -> Match:
    res = cv.matchTemplate(img, temp.img, cv.TM_CCOEFF_NORMED)   # output image (W-w+1, H-h+1)       243 x 238
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    top_left = max_loc   # (x,y)
    bottom_right = (max_loc[0] + temp.width, max_loc[1] + temp.height)    

    # If match:
    match = Match(top_left, bottom_right, temp)
    img1 = img.copy()
    match.draw(img1)
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
    print(len(matches))
    return matches 


        
def filter_matches(res: np.ndarray, expected):
    '''
    Removes duplicate matches that are most certain of the same template, resulting from not having 
    an adequate threshold value.
    @expected: the expected number of matches of image
    '''
    threshold = 0.5
    
    # or we can keep raising threshold until theres only expected amount of matches left
    locations = np.where(res >= threshold)

    while (locations[0].size > expected):       # this gets more and more selective
        threshold += 0.03
        locations = np.where(res >= threshold)
                  
    print(f'found{locations[0].size} optimal matches')
    return locations


    
