import unittest 
from coffeeshop import CoffeeShop
from coffee_finder import CoffeeFinder
from file_parser import FileParser

class TestCoffeeShop(unittest.TestCase):
    def test_error(self):
        self.assertRaises(ValueError, CoffeeShop, -1, 0)

class TestKnownResult(unittest.TestCase):
    def test_fail_one(self):
        parser = FileParser("tests/fail_test_one.txt")
        parser.get_initials()
        self.assertRaises(ValueError, parser.get_city)

    def test_fail_two(self):
        parser = FileParser("tests/fail_test_two.txt")
        parser.get_initials()
        self.assertRaises(ValueError, parser.get_city)

    def test_fail_three(self):
        parser = FileParser("tests/fail_test_three.txt")
        parser.get_initials()
        self.assertRaises(ValueError, parser.get_city)

    def test_fail_three(self):
        parser = FileParser("tests/fail_test_three.txt")
        parser.get_initials()
        self.assertRaises(ValueError, parser.get_city)

    def test_fail_four(self):
        parser = FileParser("tests/fail_test_four.txt")
        parser.get_initials()
        self.assertRaises(ValueError, parser.get_city)

    def test_fail_five(self):
        parser = FileParser("tests/fail_test_five.txt")
        parser.get_initials()
        self.assertRaises(ValueError, parser.get_city)

    def test_fail_six(self):
        parser = FileParser("tests/fail_test_six.txt")
        parser.get_initials()
        city = parser.get_city()
        self.assertRaises(ValueError, parser.get_queries)
    
    def test_success_one(self):
        parser = FileParser("tests/test_one.txt")
        parser.get_initials()
        city = parser.get_city()
        queries = parser.get_queries()
        coffee_finder = CoffeeFinder(city)
        for query in queries:
            optimum = coffee_finder.find_coffee(int(query))
            for coffee_number, cell in optimum.items():
                print("Found {0} coffeeshops near this cell: {1}".format(coffee_number, cell))

    def test_success_two(self):
        parser = FileParser("tests/test_two.txt")
        parser.get_initials()
        city = parser.get_city()
        queries = parser.get_queries()
        coffee_finder = CoffeeFinder(city)
        for query in queries:
            optimum = coffee_finder.find_coffee(int(query))
            for coffee_number, cell in optimum.items():
                print("Found {0} coffeeshops near this cell: {1}".format(coffee_number, cell))

    def test_success_three(self):
        parser = FileParser("tests/test_three.txt")
        parser.get_initials()
        city = parser.get_city()
        queries = parser.get_queries()
        coffee_finder = CoffeeFinder(city)
        for query in queries:
            optimum = coffee_finder.find_coffee(int(query))
            for coffee_number, cell in optimum.items():
                print("Found {0} coffeeshops near this cell: {1}".format(coffee_number, cell))


if __name__ == '__main__':
    unittest.main()