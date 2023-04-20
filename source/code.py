import board
import digitalio
import keypad
import supervisor
import usb_hid
from keyz.config import Config
from keyz.keyboard import Keyboard

config = Config('config')

supervisor.runtime.autoreload = False

states = [False, False, False, False]
shift = False

keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10
       )

keyboard = Keyboard(usb_hid.devices)

while True:
    event = keys.events.get()
    if event:
        # Quit if all characters pushed
        states[event.key_number] = event.pressed
        if states == [True, True, True, True]:
            continue

        row, column = keys.key_number_to_row_column(event.key_number)
        print(f'{row}, {column}')
        keycode = config.keymatrix[row][column]
        if event.pressed:
            keyboard.press(keycode)
        else:
            keyboard.release(keycode)
