from city import *


class CoffeeShop:
    # Initialize coffee shop location
    def __init__(self, x, y):
        if MIN_WIDTH_LENGTH <= x <= MAX_WIDTH_LENGTH and \
         MIN_WIDTH_LENGTH <= y <= MAX_WIDTH_LENGTH:
            self.x = x
            self.y = y
        else:
            raise ValueError("Incorrect coffee placement. Coordinates: ({0} ; {1})".format(x, y))
