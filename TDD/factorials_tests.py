import unittest

from TDD.factorials import calculate


class FactorialTests(unittest.TestCase):
    def test_factorials(self):
        self.assertEquals(calculate(1), 1)
        self.assertEquals(calculate(2), 2)
        self.assertEquals(calculate(3), 6)
        self.assertEquals(calculate(10), 3628800)


if __name__ == '__main__':
    unittest.main()
