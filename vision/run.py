
import pandas as pd
import logging 
import os 
from template import Image, Template
from collections import deque 
from vision import spreadsheet
import copy 

logging.basicConfig(format= '%(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)


from enum import Enum
class EventType(Enum):
    # this can change as more types are added 
    TIMER_FREEZE = 'TIMER_FREEZE'
    TEMPLATE_MATCH = 'TEMPLATE_MATCH'



# events with equal order means they should be sought at the same time 
class Event(): 

    def __init__(self, name, type: EventType, order):
        self.type = type
        self.name = name
        self.order = order
        self.time = ''
    
        # ---------------------- optional attributes
        self.template = None
    

    def template(self, template):
        self.template = template 
        return self
    

    def getType(self):
        return self.type.value        
    
    # def setTime(self, time): 
    #     self.time = time 
    #     logging.info(f"Recorded {self.name} at time {time}")
    
    def isFound(self) -> bool:
        return self.time != ''


    def __repr__(self):
        return f'{self.name} found at {self.time}'
    
    def clear(self):
        self.time = ''

 




NETHER_ENTRY = Event('nether', EventType.TEMPLATE_MATCH, 1).template(Image.NETHER_ENTRY),
BASTION = Event('bastion', EventType.TEMPLATE_MATCH, 2).template(Image.BASTION),
FORTRESS  =   Event('fortress', EventType.TEMPLATE_MATCH, 2).template(Image.FORTRESS),
NETHER_EXIT =  Event('nether_exit', EventType.TIMER_FREEZE, 3),
STRONGHOLD = Event('stronghold', EventType.TEMPLATE_MATCH, 4).template(Image.STRONGHOLD),
END = Event('end', EventType.TIMER_FREEZE, 5)

events = [ NETHER_ENTRY, BASTION, FORTRESS, NETHER_EXIT, STRONGHOLD, END]

# new_run = run(events) 

class Run():
    '''This is the intended object to be added into the spreadsheet, as a row. Contains events and order'''

   
    def __init__(self, events : list[Event]):             
        events.sort(key = lambda event : event.order)        # events list should be in sorted order asc
        self.events = events                                # stores actual times
        self.remaining = copy.deepcopy(self.events)         # completley new copies of events, don't want original ones in events to change 
                            
        
    def record(self, event: Event, time : str):
        if event.order == self.remaining[0].order: 
            event.time = time 
            logging.info(event.__repr__)
            self.remaining.remove(event)     

        else: logging.info("Wrong achivement order recorded")

 
    def found(self, event: Event) -> bool:
        return event.isFound()

    def seek_next(self) -> list[Event]:      # Retrieve the set of next events to be searched
        current_order = self.remaining[0].order
        seek_next = [] 
        
        for event in self.remaining:         # look for events with this order 
            if event.order == current_order: seek_next.append(event)
            if event.order > current_order: break

        return seek_next
                            

    def __repr__(self):
        return str(self.events)
    
   
    def clear(self):        # reset run and all times 
        logger.info("Starting a new run") 
        for event in self.events:
            event.clear() 
        self.remaining = self.events

        
        





