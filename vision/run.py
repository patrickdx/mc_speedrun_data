
import pandas as pd
import logging 
import os 
from template import Image, Template


logging.basicConfig(format= '%(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)


from enum import Enum
class EventType(Enum):
    TIMER_FREEZE = 'TIMER_FREEZE'
    TEMPLATE_MATCH = 'TEMPLATE_MATCH'

class Event(): 

    def __init__(self, template, name):
        # this can change as more eventTypes are added
        if template: self.type = EventType.TEMPLATE_MATCH
        else: self.type = EventType.TIMER_FREEZE

        self.template = template 
        self.name = name

    def getType(self):
        return self.type.value        
    
    # def setTime(self, time): 
    #     self.time = time 
    #     logging.info(f"Recorded {self.name} at time {time}")
    
    def isFound(self) -> bool:
        return self.time != ''


    def __repr__(self):
        return self.name
    

class Run():
    '''This is the intended object to be added into the spreadsheet, as a row. Contains events and order'''

    NETHER_ENTRY = Event(Image.NETHER_ENTRY, 'nether')
    BASTION = Event(Image.BASTION, 'bastion')
    FORTRESS =   Event(Image.FORTRESS, 'fortress')
    NETHER_EXIT =  Event(None, 'nether_exit')              # timer freeze 
    STRONGHOLD = Event(Image.STRONGHOLD, 'stronghold')
    END = Event(Image.END, 'end')

    
    def __init__(self):
        
        self.times: dict[Event] = {
            Run.NETHER_ENTRY: '', 
            Run.BASTION:  '', 
            Run.FORTRESS: '', 
            Run.NETHER_EXIT: '',              # timer freeze 
            Run.STRONGHOLD:  '', 
            Run.END: ''
        }

        self.next = Run.NETHER_ENTRY

    def record(self, event: Event, time : str):
        if event in self.next: 
            self.times[event] = time 
            logging.info(f"Recorded {event.name} at time {time}")
            self.next = seek_next()
        else: logging.info("Wrong achivement order recorded")

 
    def found(self, event: Event) -> bool:
        return self.times[event] != '' 

    def seek_next(self) -> list[Event]:      # Retrieve the set of next events to be searched
        seek = [] 
        if not self.found(Run.NETHER_ENTRY): seek = [Run.NETHER_ENTRY]

        elif self.in_nether():
            seek = [Run.FORTRESS, Run.BASTION]
            if self.found(Run.BASTION) and self.found(Run.FORTRESS): seek = [Run.NETHER_EXIT]

            # or we can say (slower)
            # seek += [Image.BASTION, Image.FORTRESS, Image.NETHER_EXIT]
        
        # nether is complete
        elif self.found(Run.NETHER_EXIT): seek = [Run.STRONGHOLD, Run.END]

        remain = [struct for struct in seek if not self.found(struct)]      # advs with time still not found yet
        logging.info(f"seeking next: {remain}")
        return remain
        

    def in_nether(self):
        return self.found(Run.NETHER_ENTRY) and not self.found(Run.NETHER_EXIT)


    def __repr__(self):
        return str(self.events)



# def test():
#     xd = run()
#     xd.record(Image.NETHER_ENTRY, '00:45')
#     print(xd.seek_next())

# test() 



        

        





