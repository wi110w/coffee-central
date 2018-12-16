from coffee_finder import CoffeeFinder
from file_parser import FileParser


parser = FileParser("tests/test_one.txt")
parser.get_initials()
city = parser.get_city()
city.print_layout()
queries = parser.get_queries()
coffee_finder = CoffeeFinder(city)
for query in queries:
    optimum = coffee_finder.find_coffee(int(query))
    for coffee_number, cell in optimum.items():
        print("Found {0} coffeeshops near this cell: {1}".format(coffee_number, cell))

print("\n")
parser = FileParser("tests/test_two.txt")
parser.get_initials()
city = parser.get_city()
city.print_layout()
queries = parser.get_queries()
coffee_finder = CoffeeFinder(city)
for query in queries:
    optimum = coffee_finder.find_coffee(int(query))
    for coffee_number, cell in optimum.items():
        print("Found {0} coffeeshops near this cell: {1}".format(coffee_number, cell))
