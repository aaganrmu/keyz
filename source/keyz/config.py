import board
from .keycode import Keycode

modes = {
    'none': 0,
    'columns': 1,
    'rows': 2,
    'layer': 3,
}


class Config(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            mode = modes['none']
            layer = ""
            self.columns = []
            self.rows = []
            self.layers = []
            self.password_stream = ""
            for line in file:
                text = line.strip("\n ")

                # ignore empty lines
                if not text:
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
                    while len(self.layers) - 1 < layer:
                        self.layers.append([])
                    continue

                # read lines using mode we're in
                if mode == modes['columns']:
                    pin = getattr(board, f'GP{text}')
                    self.columns.append(pin)
                    continue

                if mode == modes['rows']:
                    pin = getattr(board, f'GP{text}')
                    self.rows.append(pin)
                    continue

                if mode == modes['layer']:
                    keyrow = []
                    keynames = text.split(",")
                    for keyname in keynames:
                        try:
                            key = getattr(Keycode, keyname.strip(" "))
                            keyrow.append(key)
                        except AttributeError:
                            keyrow.append(keyname.strip(" "))
                    self.layers[layer].append(keyrow)
                    continue
