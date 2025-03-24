import board
from .keycode import Keycode
from keyz.keydict import keydict

modes = {
    'none': 0,
    'columns': 1, # columns for key matrix
    'rows': 2, # rows for key matrix
    'ground': 3, # Keys bound to ground
    'layer': 4, # Keys in a matrix
}


class Config(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            mode = modes['none']
            layer = ""
            self.columns = []
            self.rows = []
            self.layers = []
            self.ground = []
            for line in file:
                text = line.strip("\n ")

                # ignore empty lines and comments
                if not text:
                    continue
                if text[0] == "#":
                    continue
    
                # check to see if we're mode-switching
                try:
                    mode = modes[text]
                    continue
                except KeyError:
                    pass
                # layers are a special case
                if text[0:6] == 'layer_':
                    mode = modes['layer']
                    layer = int(text[6:])
                    # make sure we have an array that fits this layer
                    while len(self.layers) - 1 < layer:
                        self.layers.append([])
                    continue

                # Now read lines using mode we're in

                # What pins are the columns connected to?
                if mode == modes['columns']:
                    pin = getattr(board, f'GP{text}')
                    self.columns.append(pin)
                    continue

                # What pins are the rows connected to?
                if mode == modes['rows']:
                    pin = getattr(board, f'GP{text}')
                    self.rows.append(pin)
                    continue
                
                # What pins are ground pins?
                if mode == modes['ground']:
                    pin = getattr(board, f'GP{text}')
                    self.ground.append(pin)
                    continue

                # Read in a layer
                if mode == modes['layer']:
                    keyrow = []
                    keynames = text.split(" ")
                    for keyname in keynames:
                        if len(keyname) == 0:
                            continue
                        try:
                            key = keydict[keyname]
                            keyrow.append(key)
                        except KeyError:
                            keyrow.append(keyname)
                    self.layers[layer].append(keyrow)
                    continue
