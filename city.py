MIN_WIDTH_LENGTH = 1
MAX_WIDTH_LENGTH = 1000

MIN_COFFEESHOPS = 0
MAX_COFFEESHOPS = 5105


class City:
    # Initialize city with full of coffee shops
    def __init__(self, length, width, coffeeshops):
        if MIN_WIDTH_LENGTH <= width <= MAX_WIDTH_LENGTH and \
         MIN_WIDTH_LENGTH <= length <= MAX_WIDTH_LENGTH:
            self.width = width
            self.length = length
        else:
            raise ValueError("Incorrect dimensions of city. Width: {0}, length: {0}".format(width, length))
        if MIN_COFFEESHOPS <= len(coffeeshops) <= MAX_COFFEESHOPS:
            self.coffeeshops = coffeeshops
        else:
            raise ValueError("Incorrect coffee capacity. Coffeeshops: {0}".format(len(coffeeshops)))

        self.city_layout = [[None for x in range(length)] for y in range(width)]
        for coffeeshop in coffeeshops:
            self.city_layout[coffeeshop.y][coffeeshop.x] = coffeeshop

    def print_layout(self):
        for x in range(self.width):
            for y in range(self.length):
                if self.city_layout[x][y] is not None:
                    print("X", end='   ')
                else:
                    print("-", end='   ')
            print()
