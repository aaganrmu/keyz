
import keypad
import usb_hid
from keyz.config import Config
from keyz.consumer_control import ConsumerControl
from keyz.grounds import Grounds
from keyz.keyboard import Keyboard
from keyz.layer import Layer
from keyz.password import Password
from keyz.keydict import keydict
from keyz.keyaction import handlers

# setup
config = Config('config')
keys = keypad.KeyMatrix(
        config.rows, config.columns,
        max_events=10,
        columns_to_anodes=False
       )
keyboard = Keyboard(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)
layer = Layer()
password = Password()
grounds = Grounds(config.ground)

# Main loop
while True:
    # Get the next event and unpack it
    event = keys.events.get()
    if event:
        # handle key events
        row, column = keys.key_number_to_row_column(event.key_number)
    else: 
        # handle ground events if there are no key events
        event = grounds.get_event()
        if not(event):
            continue
        row = event.row
        column = event.column
    pressed = event.pressed

    # Get the action that matches the event
    try:
        action = config.layers[layer.current][row][column]
    except IndexError:
        print(f'ERROR: could not find key l{layer.current} r{row}c{column}')
        continue
    
    # Skip unused keys
    if action.handler == handlers["none"]:
        continue

    # Type normal keys
    if action.handler == handlers["key"]:
        if pressed:
            keyboard.press(action.data)
        else:
            keyboard.release(action.data)
        continue

    if action.handler == handlers["media"]:
        if pressed:
            consumer_control.press(action.data)
        else:
            consumer_control.release()
        continue

    # Layer actions
    if action.handler == handlers["layer_shift"]:
        refresh = layer.set_shift(action.data, pressed)
        if refresh:
            keyboard.release_all()
        continue

    if action.handler == handlers["layer_set"]:
        if pressed:
            refresh = layer.set_offset(action.data)
            if refresh:
                keyboard.release_all()
        continue


    #     # Do something related to password manager
    #     if case[0:9] == 'PASSWORD_':
    #         code = case[9:]
    #         password_string = password.process(code, pressed)
    #         if password_string:
    #             for character in password_string:
    #                 keycode = keydict[character]
    #                 keyboard.press(keycode)
    #                 keyboard.release(keycode)
    #             enter = keydict["ENTER"]
    #             keyboard.press(enter)
    #             keyboard.release(enter)
    #         continue