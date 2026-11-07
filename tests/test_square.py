import unittest

import square


class TestSquare(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(square.area(4.2), 4.2 ** 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(4.2), 4.2 * 4)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_perimiter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(-1)

        with self.assertRaises(ValueError):
            square.perimeter(-1)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(1 + 3j)

        with self.assertRaises(ValueError):
            square.perimeter(1 + 3j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            square.area("4.2")

        with self.assertRaises(TypeError):
            square.perimeter("4.2")
