
import digitalio
class Grounds(object):
    def __init__(self, pins = []):
        self._pins = []
        self._states = []
        for pin in pins:
            ground = digitalio.DigitalInOut(pin)
            ground.direction = digitalio.Direction.INPUT
            ground.pull = digitalio.Pull.UP
            self._pins.append(ground)
            self._states.append(False)


    def get_event(self):
        if len(self._pins) == 0:
            return
        for index, pin in enumerate(self._pins):
            pressed = not(pin.value)
            if pressed != self._states[index]:
                self._states[index] = pressed
                return {"column": index, "pressed": pressed}