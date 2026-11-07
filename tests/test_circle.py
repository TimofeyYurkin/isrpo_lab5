import unittest
import math

import circle


class TestCircle(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2), math.pi * 2 ** 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(2), 2 * math.pi * 2)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimiter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            circle.area(1 + 3j)

        with self.assertRaises(ValueError):
            circle.perimeter(1 + 3j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            circle.area("2")

        with self.assertRaises(TypeError):
            circle.perimeter("2")
