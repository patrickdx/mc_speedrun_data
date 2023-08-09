from enum import Enum
from numpy import ndarray as Mat
import numpy as np
class Frame(Enum):
    '''
    The certain subframe of the video frame to match using the template.   (top_left, bottom_right)
    Essentially places to 'look' (ROI) during the attempt to match the template.
    '''
    achievement =  ((100,100),(150,150))
    timer = ((0,0),(0,0))


    # methods for some clarity 
    def y1(self): return self.value[0][1]
    def y2(self): return self.value[1][1]
    def x1(self): return self.value[0][0]
    def x2(self): return self.value[1][0]

    def subframe(self, img : Mat):        # returns cropped version of original image 
        dim = self.value 
        x = dim[0][0], dim[1][0]
        y = dim[0][1], dim[1][1]
        return img[y[0] : y[1], x[0] : x[1]]


img = np.zeros((1000,1000))
img1 = Frame.achievement.subframe(img)
print(img1.shape)