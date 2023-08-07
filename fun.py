import numpy as np 
import cv2 as cv 

def display(title, img):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def match_single():
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED']
    for method in methods:
        img1 = img.copy()
        str = method
        method = eval(method)
        res = cv.matchTemplate(img1, template, method)   # output image (W-w+1, H-h+1)       243 x 238
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        top_left = max_loc   # (x,y)
        bottom_right = (max_loc[0] + width, max_loc[1] + height)    
        cv.rectangle(img1, top_left, bottom_right, 255, 5)       # draws a rect on img 1
        display(str, img1)


def match_multiple():
    img1 = img.copy()
    res = cv.matchTemplate(img1, template, cv.TM_CCOEFF_NORMED)
    locations = np.where(res >= 0.9)       # returns indexes of values >= 0.8 (which means higher probability of match)
    display('result', res)
    print(res)
    for pt in zip(locations[1], locations[0]):         # (rows, cols) swap them because we want (x,y) coords
        print(pt)
        cv.rectangle(img1, pt, (pt[0] + width, pt[1] + height), 255, 2)

    display('match', img1)


# img = cv.imread('images/bulldog.jpeg')      # img is internally stored as a numpy ndarray
# if img is None: raise FileNotFoundError('image not found')

# print(img.shape)    # just magine a 300x300 image with 3 channels, each pixel value is a tuple of 3

# paw = img[191:249, 169:232]    # select contiguous pixel region of height: 191-249 and width: 169-232
# img[:,:,0] = 0      # set BGR channel blue to all zeros (first value in tuple)
# display(img)

# cv.copyMakeBorder(img, 10,10,10,10, cv.BORDER_CONSTANT, value = [255,0,0])

# Template matching 
img = cv.imread('images/mario.png', cv.IMREAD_GRAYSCALE)
if img is None: raise FileNotFoundError('image not found')
template = img[289:342, 414:456]     # for rows: 191 - 249 and columns: 169:232   [y,x]    
display('xd',template)
print(template.shape)
height, width = template.shape
match_multiple()



