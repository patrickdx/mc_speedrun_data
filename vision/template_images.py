from enum import Enum 
from template import Template

folder = 'assets/'

class template_images():

    nether_entry = Template('sample.png', 'nether entry')
    bastion = Template('sample.png', 'found bastion')
    fortress: Template('sample.png', 'found fortress')
    nether_exit = Template('sample.png', 'nether exit')
    stronghold =  Template('sample.png', 'found stronghold')
    end_dimension = Template('sample.png', 'enter the end')
    dragon_kill =  Template('sample.png', 'dragon kill')
    run_finish =  Template('sample.png', 'completed run')

    zero =Template(folder + '0.png') 
    one = Template(folder + '1.png')
    two = Template(folder + '2.png')
    three = Template(folder + '3.png')
    four = Template(folder + '4.png')
    five = Template(folder + '5.png')
    six = Template(folder + '6.png')
    seven = Template(folder + '7.png')
    eight = Template(folder + '8.png')
    nine = Template(folder + '9.png')


