import board
import digitalio
import keypad
import supervisor
import time
import usb_hid
from keyz.config import Config
from keyz.keyboard import Keyboard

# setup
config = Config('config')
supervisor.runtime.autoreload = False
keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10,
        columns_to_anodes=True
       )
keyboard = Keyboard(usb_hid.devices)
layer = 0


led_onboard = digitalio.DigitalInOut(board.LED)
led_onboard.direction = digitalio.Direction.OUTPUT

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
            if key[0:7] == 'switch_':
                switch = int(key[7:])
                if event.pressed:
                    layer += switch
                    print(f'switch: ${switch}, += to ${layer}')
                else:
                    layer -= switch
                    print(f'switch: ${switch}, -= to ${layer}')
                keyboard.release_all()
            if key[0:5] == 'mode_':
                mode = int(key[5:])
                if event.pressed:
                    layer = mode
                    print(f'Set layer to ${layer}')
                    keyboard.release_all()
