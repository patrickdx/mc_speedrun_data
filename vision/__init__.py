import cv2 as cv    

def display(str, img):
    cv.imshow(str, img)
    cv.waitKey(0)
    cv.destroyAllWindows

