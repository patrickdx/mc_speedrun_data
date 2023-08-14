from enum import Enum
from numpy import ndarray as Mat
import cv2 as cv

class Match:         # class mapping Template to found matched position (x1,y1), (x2,y2)
    
    def __init__(self, pt1: tuple, pt2: tuple, template):
        self.pt1 = pt1      # the position of the match
        self.pt2 = pt2 
        self.template = template
    
    def draw(self, img):
        cv.rectangle(img, self.pt1, self.pt2, 255, 1)       # draws a rect on img 
        # cv.putText(img, self.template.desc, (self.pt1[0], self.pt1[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, 255, 1)

    def __str__(self):
        return f'{self.template.desc} match at {self.pt1} to {self.pt2}'

class Template:        # Singleton (for now)
    
    def __init__(self, path, *, value, THRESHOLD=0.8):          
        self.img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.value = value                                  # for the program to interpret the image as a value 
        assert self.img is not None, 'file not found'
        self.desc = path
        self.height, self.width = self.img.shape[0], self.img.shape[1]
        self.THRESHOLD = THRESHOLD           # how 'lenient' it should be about the successful match of a template


    def __str__(self):
        return f'{self.desc} template by {self.width} x {self.height}'


class ROI(Enum):
    '''
    The region of interest of the video frame to match using the template.   (top_left, bottom_right)
    Essentially places to 'look' during the attempt to match the template. (x1,y1) , (x2,y2)
    '''

    achievement =  ((1018,0),(1280,131))
    igt_timer = ((1121,53),(1261,72))

    def crop(self, img : Mat):        # returns cropped version of original image. for template matching purposes it should always be grayscale
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

# img = np.zeros((1000,1000))
# img1 = Frame.achievem

class Images(Enum): #https://softwareengineering.stackexchange.com/questions/357405/whats-the-most-idiomatic-way-to-make-a-collection-of-enum-enum-in-python
    IMG_PATH = '../assets/'     # TODO: find a way to write this without .. i.e. regardless of file location


    # achievements = {
    #     'nether_entry' : Template('sample.png', 'nether entry'),
    #     'bastion' : Template('sample.png', 'found bastion'),
    #     'fortress': Template('sample.png', 'found fortress'),
    #     'nether_exit' : Template('sample.png', 'nether exit'),
    #     'stronghold' :  Template('sample.png', 'found stronghold'),
    #     'end_dimension' : Template('sample.png', 'enter the end'),
    #     'dragon_kill' :  Template('sample.png', 'dragon kill'),
    #     'run_finish' :  Template('sample.png', 'completed run'),
    # }


  
    zero  = Template(IMG_PATH + '0.png', value=0)
    one  =  Template(IMG_PATH + '1.png', value=1)
    two  = Template(IMG_PATH + '2.png', value=2)
    three  =  Template(IMG_PATH + '3.png', value=3) 
    four  =  Template(IMG_PATH + '4.png', value=4)
    five  =  Template(IMG_PATH + '5.png', value=5)
    six  = Template(IMG_PATH + '6.png', value=6)
    seven  =  Template(IMG_PATH + '7.png', value=7)
    eight  =  Template(IMG_PATH + '8.png', value=8)
    nine  =  Template(IMG_PATH + '9.png', value=9)


    def template(self):
        return self.value

    @classmethod            # no longer requiring instance aka Images.zero.numbers()
    def numbers(cls):
        return [cls.zero, cls.one, cls.two, cls.three, cls.four, cls.five, cls.six, cls.seven, cls.eight, cls.nine]

    @classmethod
    def achievements(self):
        return []

