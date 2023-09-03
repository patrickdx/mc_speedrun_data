
import pandas as pd
import logging 
import os 
from template import Image, Template

ROOT_DIR = project_root = os.path.abspath(os.path.dirname(__file__))            # this is the project root 
print(ROOT_DIR)

logging.basicConfig(format= '%(levelname)s - %(message)s', level = logging.INFO)
logging.info("hello friend")

class run():

    '''This is the intended object to be added into the spreadsheet, as a row'''
    

    def __init__(self):
        
        self.sequence: dict[Template, str] = {
            Image.NETHER_ENTRY: '',
            Image.BASTION: '',
            Image.FORTRESS: '',
            Image.NETHER_EXIT: '',
            Image.STRONGHOLD: '',
            Image.END: ''
        }
        self.run_order = iter(self.sequence)
        self.current = next(self.run_order)         # the achivement ur currently looking forr


    def record(self, achivement : Template, time : str):

        # wont do anythign if already found achivement 
        if (self.current == achivement or self.current == Image.BASTION) and self.sequence[achivement] == '':   
            self.sequence[achivement] = time 
            logging.info(f"Found {achivement.value} at time {time}")
            self.current = next(self.run_order)
            logging.info(f"Seeking next: {self.current.value}")
 
        

    def next_achivement(self):
        return self.current


def test():
    xd = run()
    xd.record(Image.NETHER_ENTRY, '00:45')

test()






        

        





