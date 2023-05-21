import board
import digitalio
import keypad
import supervisor
import usb_hid
from keyz.config import Config
from keyz.keyboard import Keyboard

# setup
config = Config('config')
keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10,
        columns_to_anodes=True
       )
keyboard = Keyboard(usb_hid.devices)
layer = 0

# Main loop
while True:
    event = keys.events.get()
    if event:
        row, column = keys.key_number_to_row_column(event.key_number)
        key = config.layers[layer][row][column]

        # Push a key if a keycode is stored
        if type(key) == int:
            if event.pressed:
                keyboard.press(key)
            else:
                keyboard.release(key)

        # Do something special if it's a string
        if type(key) == str:
            # Add value to layer (for standard layers, can chord)
            if key[0:12] == 'SHIFT_LAYER_':
                switch = int(key[12:])
                if event.pressed:
                    layer += switch
                    print(f'switch: ${switch}, += to ${layer}')
                else:
                    layer -= switch
                    if layer < 0:
                        layer = 0
                    print(f'switch: ${switch}, -= to ${layer}')
                keyboard.release_all()
            # Hard set a layer (use with momentary switches)
            if key[0:10] == 'SET_LAYER_':
                mode = int(key[10:])
                if event.pressed:
                    layer = mode
                    print(f'Set layer to ${layer}')
                    keyboard.release_all()
