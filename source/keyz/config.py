import board
from .keycode import Keycode

modes = {
    'none': 0,
    'columns': 1,
    'rows': 2,
    'keys': 3
}

class Config(object):
    def __init__(self, filename):
        file = open(filename, 'r')
        mode = modes['none']
        self.columns = []
        self.rows = []
        self.keymatrix = []
        for line in file:
            text = line.strip("\n ")
            try:
                mode = modes[text]
                continue
            except KeyError:
                pass
            if mode == modes['columns']:
                pin = getattr(board, f'GP{text}')
                self.columns.append(pin)
            if mode == modes['rows']:
                pin = getattr(board, f'GP{text}')
                self.rows.append(pin)
            if mode == modes['keys']:
                keyrow = []
                keynames = text.split(",")
                for keyname in keynames:
                    key = getattr(Keycode, keyname.strip(" "))
                    keyrow.append(key)
                self.keymatrix.append(keyrow)

            print(f'{mode}: {text}')