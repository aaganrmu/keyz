import board
import keypad
import time
import usb_hid
from keyz.config import Config
from keyz.grounds import Grounds
from keyz.keyboard import Keyboard
from keyz.layer import Layer
from keyz.password import Password
from keyz.keydict import keydict

# setup
config = Config('config')
keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10,
        columns_to_anodes=False
       )
keyboard = Keyboard(usb_hid.devices)
layer = Layer()
password = Password()
grounds = Grounds(config.ground)

# Main loop
while True:
    event = keys.events.get()
    if event:
        # handle key events
        row, column = keys.key_number_to_row_column(event.key_number)
        case = config.layers[layer.current][row][column]
        pressed = event.pressed
    else: 
        # handle grounds if nothing else is happening
        event = grounds.get_event()
        if not(event):
            continue
        column = event["column"]
        pressed = event["pressed"]
        case = config.layers[layer.current][-1][column]

        print(f'Column: {column}, Pressed: {pressed}, Layer: {layer.current}, Case: {case}')
    
    # Push a key if a keycode is stored
    if type(case) == int:
        if pressed:
            keyboard.press(case)
        else:
            keyboard.release(case)
        continue

    # Do something special if it's a string
    if type(case) == str:
        # Add value to layer (for standard layers, can chord, or use with latching switches)
        if case[0:12] == 'SHIFT_LAYER_':
            shift = int(case[12:])
            refresh = layer.set_shift(shift, pressed)
            if refresh:
                keyboard.release_all()
            continue

        # Hard set a layer (use with momentary switches)
        if case[0:10] == 'SET_LAYER_':
            offset = int(case[10:])
            if pressed:
                refresh = layer.set_offset(offset)
                if refresh:
                    keyboard.release_all()
            continue

        # Do something related to password manager
        if case[0:9] == 'PASSWORD_':
            code = case[9:]
            password_string = password.process(code, pressed)
            if password_string:
                for character in password_string:
                    keycode = keydict[character]
                    keyboard.press(keycode)
                    keyboard.release(keycode)
                enter = keydict["ENTER"]
                keyboard.press(enter)
                keyboard.release(enter)
            continue