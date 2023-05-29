class Layer:
    def __init__(self):
        self._layer = 0
        self._offset = 0
        self._shifts = []

    @property
    def current(self):
        return self._layer

    def set_offset(self, offset):
        if not offset == self._offset:
            self._offset = offset
            self.update_layer()
            return True
        return False

    def set_shift(self, shift, value):
        while len(self._shifts) - 1 < shift:
            self._shifts.append(False)
        if not value == self._shifts[shift]:
            self._shifts[shift] = value
            self.update_layer()
            return True
        return False

    def update_layer(self):
        shift_total = 0
        for count, shift in enumerate(self._shifts):
            if shift:
                shift_total += count

        self._layer = self._offset + shift_total