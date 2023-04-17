from keyz.key import Key
from machine import Pin
import time
import usb_hid

led_onboard = machine.Pin(25, machine.Pin.OUT)

pins = [6, 7, 8, 9]
keys = []
for pin in pins:
    key = Key(str(pin), pin)
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
                led_onboard.on()
                time.sleep(0.1)
                led_onboard.off()
                time.sleep(0.1)
            
    i += 1
    time.sleep(0.01)

led_onboard.on()
time.sleep(1)
led_onboard.off()


