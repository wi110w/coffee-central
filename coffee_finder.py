MAX_STEPS = 106
MIN_STEPS = 1


class CoffeeFinder:
    def __init__(self, city):
        self.city = city
        self.human_to_coffee = {}

    def find_coffee(self, steps):
        if self.valid_steps(steps):
            coffee_nearby = []
            for cell_x in range(self.city.width):
                for cell_y in range(self.city.length):
                    if self.city.city_layout[cell_x][cell_y] is not None:
                        continue
                    human = (cell_x, cell_y)
                    # Begin checking if coffee is nearby
                    step = 1
                    while step <= steps:
                        # In front of human
                        if self.in_edges_and_coffee_nearby(human[0] + step, human[1]):
                            distance = self.calculate_distance(human, self.city.city_layout[cell_x + step][cell_y])
                            coffee_nearby.append(distance)
                        # Behind the human
                        if self.in_edges_and_coffee_nearby(human[0] - step, human[1]):
                            distance = self.calculate_distance(human, self.city.city_layout[cell_x - step][cell_y])
                            coffee_nearby.append(distance)
                        # Left to the human
                        if self.in_edges_and_coffee_nearby(human[0], human[1] + step):
                            distance = self.calculate_distance(human, self.city.city_layout[cell_x][cell_y + step])
                            coffee_nearby.append(distance)
                        # Right to the human
                        if self.in_edges_and_coffee_nearby(human[0], human[1] - step):
                            distance = self.calculate_distance(human, self.city.city_layout[cell_x][cell_y - step])
                            coffee_nearby.append(distance)
                        step += 1

                    if len(coffee_nearby) != 0:
                        human = (cell_y + 1, cell_x + 1)
                        self.human_to_coffee[human] = len(coffee_nearby)
                        coffee_nearby.clear()

            max_coffee_number = 0
            max_cell = set()
            optimum = {}
            for cell, coffee_number in self.human_to_coffee.items():
                if coffee_number > max_coffee_number:
                    max_coffee_number = coffee_number
                    max_cell = cell

            optimum[max_coffee_number] = max_cell

            return optimum

        raise ValueError("Invalid steps. Steps: {0}".format(steps))

    @staticmethod
    def calculate_distance(human, coffeeshop_coordinates):
        coffeeshop = coffeeshop_coordinates
        coffee = (coffeeshop.x, coffeeshop.y)
        return abs(human[0] - coffee[0]) + abs(human[1] - coffee[1])

    def in_edges_and_coffee_nearby(self, cell_x, cell_y):
        min_x = 0
        max_x = self.city.length - 1
        min_y = 0
        max_y = self.city.width - 1
        if min_x <= cell_x <= max_x and min_y <= cell_y <= max_y \
                and self.city.city_layout[cell_x][cell_y] is not None:
            return True
        return False



    @staticmethod
    def valid_steps(steps):
        return MIN_STEPS <= steps <= MAX_STEPS
