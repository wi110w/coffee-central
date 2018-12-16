MAX_STEPS = 106
MIN_STEPS = 1


class CoffeeFinder:
    def __init__(self, city):
        self.city = city
        self.human_to_coffee = {}

    def find_coffee(self, steps):
        if self.valid_steps(steps):
            for cell_y in range(self.city.width):
                for cell_x in range(self.city.length):
                    human = (cell_y, cell_x)
                    coffee_nearby_amount = self.check_moore_square(human, steps)
                    human = (cell_x + 1, cell_y + 1)
                    self.human_to_coffee[human] = coffee_nearby_amount

            max_coffee_number = 0
            min_y = self.city.width
            min_x = self.city.length
            max_cell = set()
            optimum = {}
            # Find the optimum
            for cell, coffee_number in self.human_to_coffee.items():
                if coffee_number > max_coffee_number:
                    max_coffee_number = coffee_number
                    max_cell = cell

            # Find the optimal location
            for cell, coffee_number in self.human_to_coffee.items():
                if coffee_number == max_coffee_number:
                    if cell[0] < min_y and cell[1] < min_x:
                        min_x = cell[1]
                        min_y = cell[0]
                        max_cell = cell

            optimum[max_coffee_number] = max_cell

            return optimum

        raise ValueError("Invalid steps. Steps: {0}".format(steps))

    # Checking cells around the human if there is any coffee
    def check_moore_square(self, human, radius):
        coffee_nearby_amount = 0
        for cell_y in range(human[0] - radius, human[0] + (radius + 1)):
            if cell_y < 0 or cell_y >= self.city.width:
                continue
            for cell_x in range(human[1] - radius, human[1] + (radius + 1)):
                if cell_x < 0 or cell_x >= self.city.length:
                    continue
                cell = (cell_y, cell_x)
                distance = self.calculate_distance(human, cell)
                if distance <= radius:
                    if self.is_coffee_nearby(cell_y, cell_x):
                        coffee_nearby_amount += 1
        return coffee_nearby_amount

    @staticmethod
    def calculate_distance(human, cell):
        return abs(human[0] - cell[0]) + abs(human[1] - cell[1])

    def is_coffee_nearby(self, cell_y, cell_x):
        return self.city.city_layout[cell_y][cell_x] is not None

    @staticmethod
    def valid_steps(steps):
        return MIN_STEPS <= steps <= MAX_STEPS
