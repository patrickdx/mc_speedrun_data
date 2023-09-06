
import pandas as pd
import logging 
import os 
from template import Image, Template

ROOT_DIR = project_root = os.path.abspath(os.path.dirname(__file__))            # this is the project root 
print(ROOT_DIR)

logging.basicConfig(format= '%(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)



# try to match everything approach, maybe slower?
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


        # self.run_order = iter(self.sequence)
        # self.current = next(self.run_order)         # the achivement ur currently looking forr


    def record(self, achievement : Template, time : str):
        logging.info(f'looking for {achievement.value}')
        # wont do anythign if already found achivement 
        if self.sequence[achievement] == '':   
            self.sequence[achievement] = time
            logging.info(f"Found {achievement.value} at time {time}")
        
        else: logging.info("achivement already found")
 


    def check_valid(self, adv: Template) -> bool:         # checks if adv is ok to add to run 
        completed = [key for key in self.sequence if self.sequence[key] != '']
        # simple checks to validate the run 
        if (adv == Image.BASTION or adv == Image.FORTRESS) and Image.NETHER_ENTRY not in completed: return False
        if adv == Image.STRONGHOLD and (Image.NETHER_ENTRY not in completed or Image.NETHER_EXIT not in completed): return False
        assert time[Image.NETHER_EXIT] > Image.FORTRESS, 'invalid'
        return True 


    def export(self):
        self.check_valid()
        pass 
        


def test():
    xd = run()
    xd.record(Image.NETHER_ENTRY, '00:45')
    

test()







        

        





