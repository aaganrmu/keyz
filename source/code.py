import board
import digitalio
import keypad
import supervisor
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

supervisor.runtime.autoreload = False


columns = [
           board.GP9
          ]

rows = [
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13
       ]
states = [False, False, False, False]
shift = False

keys = keypad.KeyMatrix(
        rows, columns,
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
            print("X")
            keyboard.press(keycode)
        else:
            print("O")
            keyboard.release(keycode)
