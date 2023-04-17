import board
import digitalio
import time
import usb_hid
from keyz.key import Key

led_onboard = digitalio.DigitalInOut(board.LED)
led_onboard.direction = digitalio.Direction.OUTPUT

pins = [
        [board.GP6, 'shift'],
        [board.GP7, 'a'],
        [board.GP8, 'b'],
        [board.GP9, 'c']
       ]
keys = []

for pin in pins:
    key = Key(pin[1], pin[0])
    keys.append(key)

keys[0].modifier = True

i = 0
while i < 1000:
    string = ""
    for key in keys:
        if key.poll():
            if keys[0].state:
                times = 2
            else:
                times = 1
            for i in range(times):
                led_onboard.value = 1
                time.sleep(0.1)
                led_onboard.value = 0
                time.sleep(0.1)
            
    i += 1
    time.sleep(0.01)

led_onboard.on()
time.sleep(1)
led_onboard.off()


