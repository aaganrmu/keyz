import board
import digitalio
import keypad
import time
import usb_hid

led_onboard = digitalio.DigitalInOut(board.LED)
led_onboard.direction = digitalio.Direction.OUTPUT

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

while True:
    event = keys.events.get()
    if event:
        print(event)
        states[event.key_number] = event.pressed
        if event.key_number == 0:
            shift = event.pressed
        if event.key_number in [1,2,3]:
            if event.pressed:
                times = 1 if not shift else 2
                for i in range(times*2):
                    led_onboard.value = not led_onboard.value    
                    time.sleep(0.1)                



for i in range(8):
    led_onboard.value = not led_onboard.value    
    time.sleep(0.1)