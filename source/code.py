import board
import digitalio
import keypad
import time
import usb_hid
from keyz.config import Config
from keyz.keyboard import Keyboard
from keyz.layer import Layer
from keyz.password import Password
from keyz.keydict import keydict

# setup
config = Config('config')
keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10,
        columns_to_anodes=True
       )
keyboard = Keyboard(usb_hid.devices)
layer = Layer()
password = Password()

# Main loop
while True:
    event = keys.events.get()
    if event:
        row, column = keys.key_number_to_row_column(event.key_number)
        key = config.layers[layer.current][row][column]
        # Push a key if a keycode is stored
        if type(key) == int:
            if event.pressed:
                keyboard.press(key)
            else:
                keyboard.release(key)

        # Do something special if it's a string
        if type(key) == str:

            # Add value to layer (for standard layers, can chord, or use with latching switches)
            if key[0:12] == 'SHIFT_LAYER_':
                shift = int(key[12:])
                refresh = layer.set_shift(shift, event.pressed)
                if refresh:
                    keyboard.release_all()

            # Hard set a layer (use with momentary switches)
            if key[0:10] == 'SET_LAYER_':
                offset = int(key[10:])
                if event.pressed:
                    refresh = layer.set_offset(offset)
                    if refresh:
                        keyboard.release_all()

            # Do somethin related to password manaer
            if key[0:9] == 'PASSWORD_':
                code = key[9:]
                password_string = password.process(code, event.pressed)
                if password_string:
                    for character in password_string:
                        keycode = keydict[character]
                        keyboard.press(keycode)
                        keyboard.release(keycode)
                    enter = keydict["ENTER"]
                    keyboard.press(enter)
                    keyboard.release(enter)