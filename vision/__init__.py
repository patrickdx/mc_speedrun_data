# this gets executed when import vision, all stuff is added to vision package namespace


import cv2 as cv    

def display(str, img):
    cv.imshow(str, img)
    cv.waitKey(0)
    cv.destroyAllWindows

something = 5

print(dir())