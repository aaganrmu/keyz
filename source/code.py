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

keycodes = [Keycode.A, Keycode.B, Keycode.C]

keyboard = Keyboard(usb_hid.devices)

while True:
    event = keys.events.get()
    if event:
        states[event.key_number] = event.pressed
        if event.key_number == 0:
            shift = event.pressed
        if event.key_number in [1,2,3]:
            if event.pressed:
                if states[1:4] == [True, True, True]:
                    break
                keycode = keycodes[event.key_number-1]
                if shift:
                    keyboard.send(Keycode.LEFT_SHIFT, keycode)
                else:
                    keyboard.send(keycode)
