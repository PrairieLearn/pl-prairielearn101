import prairielearn as pl
import pygraphviz
import numpy as np
from os import path


# Import class definitions and default values from the drawing element
defaults = pl.load_host_script('defaults.py')
elements = pl.load_host_script('elements.py')

# Elements
class PushButton(elements.BaseElement):
    def generate(el, data):
        image = 'push-button-' + str(pl.get_integer_attrib(el, 'npins', 4)) + '.svg'
        return {
            'left': pl.get_float_attrib(el, 'x', 100),
            'top': pl.get_float_attrib(el, 'y', 100),
            'angle': pl.get_float_attrib(el, 'angle', 0),
            'npins': pl.get_integer_attrib(el, 'npins', 4),
            'image_url': path.join(data['clientFilesUrl'], image)
        }

    def get_attributes():
        return ['x', 'y', 'npins', 'angle']


elements = {}
elements['pl-push-button'] = PushButton
