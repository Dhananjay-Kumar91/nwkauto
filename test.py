from jinja2 import Environment, FileSystemLoader
import yaml
from bracket_expansion import *

ENV = Environment(loader = FileSystemLoader('/Users/ENIGMA/ENGIGMA\'S MACBOOK/Network Automation/nwkauto-master/2-jinja2/templates'))

def gen(filename):
    print('-----------------------------------')
    print('')
    with open('/Users/ENIGMA/ENGIGMAS_MACBOOK/Network_Automation/nwkauto-master/2-jinja2/vars/' + filename + '.yml') as _:
    varfile = yaml.load(_)
    template = ENV.get_template(filename + '.j2')
    print (template.render(config=varfile))
