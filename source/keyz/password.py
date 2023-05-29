class Password:
    def __init__(self, pad):
        self._pad = pad
        self._stream = ""

    def process(self, code):
        print(code)