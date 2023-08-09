import cv2 as cv

class Match:

    def __init__(self, pt1: tuple, pt2: tuple, template):
        self.pt1 = pt1      # the position of the match
        self.pt2 = pt2 
        self.template = template
    
    def drawRect(self, img):
        cv.rectangle(img, self.pt1, self.pt2, 255, 5)       # draws a rect on img 1

    def __str__(self):
        return f'{self.template.desc} match at {self.pt1} and {self.pt2} '


class Template:        # Singleton (for now)
    
    def __init__(self, desc, path, THRESHOLD=0.8):
        self.img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.desc = desc 
        self.height, self.width = self.img.shape[0], self.img.shape[1]
        self.THRESHOLD = THRESHOLD           # how 'lenient' it should be about the successful match of a template


    def __str__(self):
        return f'{self.desc} template by {self.width} x {self.height}'
    

def display(title, img):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()