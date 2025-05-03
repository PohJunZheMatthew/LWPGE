class brightnessOutOfBounds(Exception):
    def __init__(self):
        super().__init__("BrightnessOutOfBounds: Please put a value from 0 to 100")
class failedToInitializationShape(Exception):
    def __init__(self):
        super().__init__("failedToInitializationShape: Please create the shapeArray properly")
