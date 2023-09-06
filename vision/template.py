from enum import Enum
from numpy import ndarray as Mat
import cv2 as cv
import os 
from typing import Iterator

class Match:         # Wrapper template class with a matched position (x1,y1), (x2,y2)
    
    def __init__(self, pt1: tuple, pt2: tuple, template):
        self.pt1 = pt1      
        self.pt2 = pt2 
        self.template = template
    
    def draw(self, img):
        cv.rectangle(img, self.pt1, self.pt2, 255, 1)       # draws a rect on img 
        # cv.putText(img, self.template.desc, (self.pt1[0], self.pt1[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, 255, 1)

    def __str__(self):
        return f'{self.template.value} match at {self.pt1} to {self.pt2}'

class Template:        
    
    def __init__(self, path, *, value, THRESHOLD=0.8):          
        self.img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.value = value                                  # for the program to interpret the image as a value 
        assert self.img is not None, 'file not found'
        self.height, self.width = self.img.shape[0], self.img.shape[1]
        self.THRESHOLD = THRESHOLD           # how 'lenient' it should be about the successful match of a template


    def __str__(self):
        return f'{self.value}'
    
    def __repr__(self) -> str:      # called when printing objects in list, for debugging purposes
        return str(self)

class ROI(Enum):        # enum is better because immutable/iterable/can define functionality on the enum members.
    '''
    The region of interest of the video frame to match using the template.   (top_left, bottom_right)
    Essentially places to 'look' during the attempt to match the template. (x1,y1) , (x2,y2)
    '''

    achievement =  ((1018,0),(1280,131))
    igt_timer = ((1166,53), (1259, 71))

    def crop(self, img : Mat):        # returns cropped version of original image. for template matching purposes it should always be grayscale (igt_timer.crop())
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        dim = self.value 
        x = dim[0][0], dim[1][0]
        y = dim[0][1], dim[1][1]

        crop = (img_gray[y[0] : y[1], x[0] : x[1]])
        return crop

    
    def __str__(self):
        pt1 = self.value[0]
        pt2 = self.value[1]
        return f'{pt1} x {pt2}'



class Image():
    IMG_PATH = '../assets/'     # TODO: find a way to write this without .. i.e. regardless of file location, .. is relative to where template.py is run

    NETHER_ENTRY = Template(IMG_PATH + 'adv_nether.png', value = 'nether_entry')
    BASTION = Template(IMG_PATH + 'adv_bastion.png', value = 'bastion')
    FORTRESS = Template(IMG_PATH + 'adv_fortress.png', value = 'fortress')
    NETHER_EXIT = Template(IMG_PATH + 'adv_nether.png', value = 'nether_exit')         # this should be found using timer freeze
    STRONGHOLD = Template(IMG_PATH + 'adv_stronghold.png', value = 'stronghold')
    END = Template(IMG_PATH + 'adv_end.png', value = 'end')
    RUN_FINISH = Template(IMG_PATH + 'adv_nether.png', value = 'finished')             # maybe better way of detecting when run is over 

  
    ZERO  = Template(IMG_PATH + '0.png', value=0, THRESHOLD= 0.9)
    ONE  =  Template(IMG_PATH + '1.png', value=1, THRESHOLD= 0.8)
    TWO  = Template(IMG_PATH + '2.png', value=2, THRESHOLD= 0.9)
    THREE  =  Template(IMG_PATH + '3.png', value=3, THRESHOLD= 0.9) 
    FOUR  =  Template(IMG_PATH + '4.png', value=4, THRESHOLD= 0.9)
    FIVE  =  Template(IMG_PATH + '5.png', value=5, THRESHOLD= 0.9)
    SIX  = Template(IMG_PATH + '6.png', value=6, THRESHOLD= 0.9)
    SEVEN  =  Template(IMG_PATH + '7.png', value=7, THRESHOLD= 0.9)
    EIGHT  =  Template(IMG_PATH + '8.png', value=8, THRESHOLD= 0.9)
    NINE  =  Template(IMG_PATH + '9.png', value=9, THRESHOLD= 0.9)

    def numbers() -> tuple[Template]:
        return (Image.ZERO, Image.ONE, Image.TWO, Image.THREE, Image.FOUR, Image.FIVE, Image.SIX, Image.SEVEN, Image.EIGHT, Image.NINE)

    def achievements() -> list[Template]:
        return [Image.NETHER_ENTRY, Image.BASTION, Image.FORTRESS, Image.NETHER_EXIT, Image.STRONGHOLD, Image.END, Image.RUN_FINISH]

    def run_order() -> list[Template]:
        return [Image.NETHER_ENTRY, [Image.BASTION, Image.FORTRESS], Image.NETHER_EXIT, Image.STRONGHOLD, Image.END]    # [] is when order doesnt matter 

    