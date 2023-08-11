from enum import Enum
from match import Template
from Frame import Frame

XD = 5

class Milestone(Enum):      
    
    nether_entry = Template('sample.png', 'nether entry')
    bastion = Template('sample.png', 'found bastion')
    fortress: Template('sample.png', 'found fortress')
    nether_exit = Template('sample.png', 'nether exit')
    stronghold =  Template('sample.png', 'found stronghold')
    end_dimension = Template('sample.png', 'enter the end')
    dragon_kill =  Template('sample.png', 'dragon kill')
    run_finish =  Template('sample.png', 'completed run')


