class KeyAction:
    def __init__(self, handler = "none", data = None):
        self.handler = handler
        self.data = data

def handlers = {
    "none":        0 # Unbound keys
    "key":         1 # Normal keyboard keys
    "media":       2 # Media keys
    "layer_shift": 3 # Shift a layer while key is held
    "layer_set":   4 # Set a layer offset
}