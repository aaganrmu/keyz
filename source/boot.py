import time
import board
import digitalio

led_onboard = digitalio.DigitalInOut(board.LED)
led_onboard.direction = digitalio.Direction.OUTPUT

pauses = [0.1, 0.5, 0.0]

for pause in pauses:
    led_onboard.value = True
    time.sleep(0.1)
    led_onboard.value = False
    time.sleep(time)
