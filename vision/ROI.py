from enum import Enum
from numpy import ndarray as Mat
import numpy as np
class Frame(Enum):
    '''
    The region of interest of the video frame to match using the template.   (top_left, bottom_right)
    Essentially places to 'look' during the attempt to match the template. (x1,y1) , (x2,y2)
    '''
    achievement =  ((1018,0),(1280,131))
    igt_timer = ((1121,53),(1261,72))

    def crop(self, img : Mat):        # returns cropped version of original image 
        dim = self.value 
        x = dim[0][0], dim[1][0]
        y = dim[0][1], dim[1][1]

        crop = (img[y[0] : y[1], x[0] : x[1]])
        return crop


# img = np.zeros((1000,1000))
# img1 = Frame.achievement.subframe(img)
# print(img1.shape)