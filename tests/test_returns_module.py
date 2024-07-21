from ast import List
import unittest
from src.methods.generate_returns import generate_value, generate_returns


class TestMyModule(unittest.TestCase):
    def test_generate_value(self):
        self.assertGreater(generate_value(.50), 0)

    def test_generate_value(self):
        self.assertIsInstance((generate_returns(10), 10), List)


if __name__ == '__main__':
    unittest.main()
