import prairielearn as pl
import pygraphviz
import numpy as np
from os import path


# Import class definitions and default values from the drawing element
defaults = pl.load_host_script('defaults.py')
elements = pl.load_host_script('elements.py')

# Elements
class Resistor(elements.BaseElement):
    def generate(el, data):
        image = 'resistor-' + str(pl.get_integer_attrib(el, 'ohm', 1000)) + '.svg'
        return {
            'left': pl.get_float_attrib(el, 'x', 100),
            'top': pl.get_float_attrib(el, 'y', 100),
            'angle': pl.get_float_attrib(el, 'angle', 0),
            'ohm': pl.get_integer_attrib(el, 'ohm', 1000),
            'image_url': path.join(data['clientFilesUrl'], image)
        }

    def get_attributes():
        return ['x', 'y', 'ohm', 'angle']


elements = {}
elements['pl-resistor'] = Resistor
