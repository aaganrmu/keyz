import digitalio
import board

class Key(object):
    def __init__(self, name, pin):
        super().__init__()

        self._button = digitalio.DigitalInOut(pin)
        self._button.switch_to_input(pull=digitalio.Pull.UP)
        self._state = not self._button.value
        self.modifier = False
        self.name = name

    @property
    def state(self):
        return self._state

    def poll(self):
        new_state = not self._button.value
        if self._state != new_state:
            self._state = new_state
            if (not self.modifier) and new_state:
                return True

