import board
import digitalio
import keypad
import supervisor
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

supervisor.runtime.autoreload = False

pins = [
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9
       ]
states = [False, False, False, False]
shift = False

keys = keypad.Keys(
        pins=pins,
        value_when_pressed=False,
        pull=True,
        max_events=10
       )

keycodes = [Keycode.LEFT_SHIFT, Keycode.A, Keycode.B, Keycode.C]

keyboard = Keyboard(usb_hid.devices)

while True:
    event = keys.events.get()
    if event:
        # Quit if all characters pushed
        states[event.key_number] = event.pressed
        if states[1:4] == [True, True, True]:
            keyboard.release_all()
            break

        keycode = keycodes[event.key_number]
        if event.pressed:
            keyboard.press(keycode)
        else:
            keyboard.release(keycode)
