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

keys = keypad.Keys(
        pins=pins,
        value_when_pressed=False,
        pull=True,
        max_events=10
       )

i = 0
while i<100:

time.sleep(1)
led_onboard.on()
time.sleep(1)
led_onboard.off()
time.sleep(1)
led_onboard.on()
time.sleep(1)
led_onboard.off()


