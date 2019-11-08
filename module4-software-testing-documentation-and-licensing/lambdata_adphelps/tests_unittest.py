import random
import unittest
import df_utils


class TestCat(unittest.TestCase):
    def setUp(self):
        self.test_age = random.randint(0, 100)
        self.cat = df_utils.Cat(age=self.test_age, weight=20)

    def test_repr(self):
        self.assertEqual(repr(self.cat), f'Cat(age={self.test_age})')

    def test_str(self):
        self.assertEqual(
            str(self.cat), f"This is a cat that's {self.test_age} years old")


if __name__ == '__main__':
    unittest.main()
