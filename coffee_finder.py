MAX_STEPS = 106
MIN_STEPS = 1


class CoffeeFinder:
    def __init__(self, city):
        self.city = city
        self.human_to_coffee = {}

    def find_coffee(self, steps):
        if self.valid_steps(steps):
            coffee_nearby = []
            city_layout = self.city.city_layout
            for cell_y in range(self.city.width):
                for cell_x in range(self.city.length):
                    if city_layout[cell_y][cell_x] is not None:
                        continue
                    human = (cell_y, cell_x)
                    # Begin checking if coffee is nearby
                    step = 1
                    while step <= steps:
                        # In front of human
                        if self.in_edges_and_coffee_nearby(human[0] + step, human[1]):
                            distance = self.calculate_distance(human, city_layout[cell_y + step][cell_x], steps)
                            self.check_and_add_distance(distance, coffee_nearby)
                        # Behind the human
                        if self.in_edges_and_coffee_nearby(human[0] - step, human[1]):
                            distance = self.calculate_distance(human, city_layout[cell_y - step][cell_x], steps)
                            self.check_and_add_distance(distance, coffee_nearby)
                        # Left to the human
                        if self.in_edges_and_coffee_nearby(human[0], human[1] + step):
                            distance = self.calculate_distance(human, city_layout[cell_y][cell_x + step], steps)
                            self.check_and_add_distance(distance, coffee_nearby)
                        # Right to the human
                        if self.in_edges_and_coffee_nearby(human[0], human[1] - step):
                            distance = self.calculate_distance(human, city_layout[cell_y][cell_x - step], steps)
                            self.check_and_add_distance(distance, coffee_nearby)

                        # If steps more than one, check if there is coffee nearby
                        if steps > 1:
                            # Front-left to the human
                            if self.in_edges_and_coffee_nearby(human[0] + step, human[1] + step):
                                distance = self.calculate_distance(human, city_layout[cell_y + step][cell_x + step], steps)
                                self.check_and_add_distance(distance, coffee_nearby)
                            # Front-right to the human
                            if self.in_edges_and_coffee_nearby(human[0] + step, human[1] - step):
                                distance = self.calculate_distance(human, city_layout[cell_y + step][cell_x - step], steps)
                                self.check_and_add_distance(distance, coffee_nearby)
                            # Behind-left to the human
                            if self.in_edges_and_coffee_nearby(human[0] - step, human[1] + step):
                                distance = self.calculate_distance(human, city_layout[cell_y - step][cell_x + step], steps)
                                self.check_and_add_distance(distance, coffee_nearby)
                            # Behind-right to the human
                            if self.in_edges_and_coffee_nearby(human[0] - step, human[1] - step):
                                distance = self.calculate_distance(human, city_layout[cell_y - step][cell_x - step], steps)
                                self.check_and_add_distance(distance, coffee_nearby)
                        step += 1

                    if len(coffee_nearby) != 0:
                        human = (cell_x + 1, cell_y + 1)
                        self.human_to_coffee[human] = len(coffee_nearby)
                        coffee_nearby.clear()

            max_coffee_number = 0
            min_y = self.city.width
            min_x = self.city.length
            max_cell = set()
            optimum = {}
            for cell, coffee_number in self.human_to_coffee.items():
                if coffee_number > max_coffee_number:
                    max_coffee_number = coffee_number
                    max_cell = cell

            for cell, coffee_number in self.human_to_coffee.items():
                if coffee_number == max_coffee_number:
                    if cell[0] < min_y and cell[1] < min_x:
                        min_x = cell[1]
                        min_y = cell[0]
                        max_cell = cell

            optimum[max_coffee_number] = max_cell

            return optimum

        raise ValueError("Invalid steps. Steps: {0}".format(steps))

    @staticmethod
    def calculate_distance(human, coffeeshop_coordinates, steps):
        coffeeshop = coffeeshop_coordinates
        coffee = (coffeeshop.y, coffeeshop.x)
        distance = abs(human[0] - coffee[0]) + abs(human[1] - coffee[1])
        if distance <= steps:
            return distance
        return 0

    def in_edges_and_coffee_nearby(self, cell_y, cell_x):
        min_x = 0
        max_x = self.city.length - 1
        min_y = 0
        max_y = self.city.width - 1
        if min_x <= cell_x <= max_x and min_y <= cell_y <= max_y \
                and self.city.city_layout[cell_y][cell_x] is not None:
            return True
        return False

    @staticmethod
    def check_and_add_distance(distance, coffee_nearby):
        if distance != 0:
            coffee_nearby.append(distance)

    @staticmethod
    def valid_steps(steps):
        return MIN_STEPS <= steps <= MAX_STEPS
