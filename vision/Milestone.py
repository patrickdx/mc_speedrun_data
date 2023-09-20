# 3 possible things to look for in run: timer freeze, achievemnt, hotbar, ... 
from abc import ABC, abstractmethod
# from package.vision.template import *
from package.vision.matcher import match_Template, seek_achievements, seek_timer

EVENTS = [hotbar, achievement, timer_freeze]

class Milestone():

    def __init__(self, type, template = None):
        self.type = type
        self.template = template 


    



# class Hotbar(Milestone):
#     def search(self, xd):
#         print(xd)

# for milestones in Milestone:
#     if (milestone.search() != None) run.record(milestone, seek_timer(frame))
# xd = Hotbar().search("ASDASDS")

# for milestone in Milestones:
#     milestone.search()  

