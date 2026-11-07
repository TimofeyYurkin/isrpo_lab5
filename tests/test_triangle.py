import unittest
import itertools

import triangle


class TestTriangle(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(1.2, 3.0), 1.2 * 3.0 / 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 1.5 + 2.5 + 3.0)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(1, 0), 0)

    def test_area_zero_side(self):
        self.assertEqual(triangle.area(0, 1), 0)

    def test_perimiter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_order_independent(self):
        sides = (3, 4, 5)

        for switched_sides in itertools.permutations(sides):
            self.assertEqual(triangle.perimeter(*sides), triangle.perimeter(*switched_sides))

    def test_perimeter_inequality_raises(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 10)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, -2)

        with self.assertRaises(ValueError):
            triangle.perimeter(-3, -4, -5)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            triangle.area(1 + 3j, 2 - 4j)

        with self.assertRaises(ValueError):
            triangle.perimeter(-4 + 7j, 9 + 1j, 1 - 6j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            triangle.area("10.1", "1.2")

        with self.assertRaises(TypeError):
            triangle.perimeter("3", "4", "5")
