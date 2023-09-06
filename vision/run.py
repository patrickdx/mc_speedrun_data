
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
        
        self.times: dict[Template, str] = {
            Image.NETHER_ENTRY: '',
            Image.BASTION: '',
            Image.FORTRESS: '',
            Image.NETHER_EXIT: '',          # iff above 2 are completed
            Image.STRONGHOLD: '',
            Image.END: ''
        }


    def record(self, achivement : Template, time : str):
        self.times[achivement] = time 
        logging.info(f"Recorded {achivement.value} at time {time}")

 
    
    def found(self, adv: Template) -> bool:
        return self.times[adv] != ''

    # this is with the idea that you bother to match adv already found, so not that slow 
    def seek_next(self) -> list[Template]:      # would be called to obtain next adv to be searched
        seek = [] 
        if not self.found(Image.NETHER_ENTRY): seek += [Image.NETHER_ENTRY]

        elif self.in_nether():
            # if not self.found(Image.BASTION): seek.append(Image.BASTION)      if we define such an order, may have some problems
            # if not self.found(Image.FORTRESS): seek.append(Image.FORTRESS)
            # if self.found(Image.BASTION) and self.found(Image.FORTRESS): seek.append(Image.NETHER_EXIT)

            # or we can say 
            seek += [Image.BASTION, Image.FORTRESS, Image.NETHER_EXIT]
        
        # nether is complete
        elif self.found(Image.NETHER_EXIT): seek += [Image.STRONGHOLD, Image.END]

        remain = [struct for struct in seek if not self.found(struct)]   # advs with time still not found yet
        logging.info(f"seeking next: {remain}")
        return remain
        

    def in_nether(self):
        return self.found(Image.NETHER_ENTRY) and not self.found(Image.NETHER_EXIT)

    def __repr__(self) -> str:
        return str(self.times)
        


# def test():
#     xd = run()
#     xd.record(Image.NETHER_ENTRY, '00:45')
#     print(xd.seek_next())

# test() 



        

        





