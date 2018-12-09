from city import City
from coffeeshop import CoffeeShop

MIN_QUERY = 1
MAX_QUERY = 20
END_FILE = '0 0 0 0'


class FileParser:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.lines = self.file.readlines()
        self.lines.reverse()
        self.file.close()
        self.first_line = ''

    # Initial integers: city size, number of coffeeshops and queries
    def get_initials(self):
        self.first_line = self.lines.pop()
        if self.first_line == END_FILE:
            print("Reached end file. Exiting...")
            return 0
        self.first_line = self.first_line.split()
        if len(self.first_line) != 4:
            raise ValueError("Four integers expected, got {0}".format(len(self.first_line)))

    def get_city(self):
        coffee_number = self.first_line[2]
        coffee_coordinates = []
        str_coordinates = 4     # For reading each coordinates (+ \n) until got queries with size in one symbol
        i = len(self.lines) - 1
        while len(self.lines[i]) == str_coordinates:
            coffee_coordinates.append(self.lines.pop())
            i -= 1
        if len(coffee_coordinates) != int(coffee_number):
            raise ValueError("Read coffeeshop placements don't match with given "
                             "number of it. Expected: {0}, actual: {1}".format(coffee_number,
                             len(coffee_coordinates)))
        coffeeshops = []
        for str_coffee_coordinate in coffee_coordinates:
            coffee_coordinate = str_coffee_coordinate.split()
            coffeeshops.append(CoffeeShop(int(coffee_coordinate[0]), int(coffee_coordinate[1])))

        return City(int(self.first_line[0]), int(self.first_line[1]), coffeeshops)

    def get_queries(self):
        query_number = self.first_line[3]
        if int(query_number) > MAX_QUERY:
            raise ValueError("Exceeded query limit({0}). Queries: {1}".format(MAX_QUERY, len(queries)))
        queries = []
        str_query = 2
        i = len(self.lines) - 1
        while len(self.lines[i]) == str_query:
            queries.append(self.lines.pop())
            i -= 1
        if len(queries) != int(query_number):
            raise ValueError("Read queries don't match with given number of it. "
                             "Expected: {0}, actual: {1}".format(query_number, len(queries)))

        return queries



