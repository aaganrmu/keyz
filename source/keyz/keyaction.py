
handlers = {
    "none":        0, # Unbound keys
    "key":         1, # Normal keyboard keys
    "media":       2, # Media keys
    "layer_add":   3, # Add to layer offset while key is held
    "layer_set":   4, # Set a layer offset
    "password":    5, # Password generator
}

class KeyAction:
    def __init__(self, handler = 0, data = None):
        self.handler = handler
        self.data = data
