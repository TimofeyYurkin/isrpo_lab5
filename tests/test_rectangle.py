import unittest

import rectangle


class TestRectangle(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(3.5, 1.7), 3.5 * 1.7)

    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle.perimeter(3.5, 1.7), (3.5 + 1.7) * 2)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_perimiter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, -2)

        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, -2)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            rectangle.area(1 + 3j, -6 + 5j)

        with self.assertRaises(ValueError):
            rectangle.perimeter(1 + 3j, -6 + 5j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            rectangle.area("3.5", "1.7")

        with self.assertRaises(TypeError):
            rectangle.perimeter("3.5", "1.7")
