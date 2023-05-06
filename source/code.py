import board
import digitalio
import keypad
import supervisor
import usb_hid
from keyz.config import Config
from keyz.keyboard import Keyboard

# setup
config = Config('config')
supervisor.runtime.autoreload = False
keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10
       )
keyboard = Keyboard(usb_hid.devices)
layer = 0

while True:
    event = keys.events.get()
    if event:
        row, column = keys.key_number_to_row_column(event.key_number)
        key = config.layers[layer][row][column]
        if type(key) == int:
            if event.pressed:
                keyboard.press(key)
            else:
                keyboard.release(key)
        if type(key) == str:
            print(key[:7])
            if key[0:7] == 'switch_':
                switch = int(key[7:])
                print(switch)
                if event.pressed:
                    layer += switch
                    print(f'switch: ${switch}, += to ${layer}')
                else:
                    layer -= switch
                    print(f'switch: ${switch}, -= to ${layer}')
                keyboard.release_all()