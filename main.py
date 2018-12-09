from coffee_finder import CoffeeFinder
from file_parser import FileParser


parser = FileParser("test.txt")
exit_code = parser.get_initials()
if exit_code == 0:
    exit(0)
city = parser.get_city()
city.print_layout()
queries = parser.get_queries()
coffee_finder = CoffeeFinder(city)
for query in queries:
    optimum = coffee_finder.find_coffee(int(query))
    for coffee_number, cell in optimum.items():
        print("Found {0} coffeeshops near this cell: {1}".format(coffee_number, cell))
