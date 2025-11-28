import unittest

def area(a, h):
    """
    Возвращает площадь треугольника.
    
    Параметры:
        a (float): основание треугольника
        h (float): высота треугольника
    
    Возвращаемое значение:
        area (float): площадь треугольника
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Возвращает периметр треугольника.
    
    Параметры:
        a (float): первая сторона треугольника
        b (float): вторая сторона треугольника
        c (float): третья сторона треугольника
    
    Возвращаемое значение:
        perimeter (float): периметр треугольника
    """
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    """
    Тесты для функций площади и периметра треугольника
    """
    
    
    def test_area_positive_integers(self):
        """Тест площади с положительными целыми числами"""
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(6, 4), 12)
    
    def test_area_positive_floats(self):
        """Тест площади с положительными дробными числами"""
        self.assertAlmostEqual(area(5.5, 3.2), 8.8)
        self.assertAlmostEqual(area(2.5, 4.0), 5.0)
    
    def test_area_both_zero(self):
        """Тест площади с нулевыми основанием и высотой"""
        self.assertEqual(area(0, 0), 0)
    
    def test_area_large_numbers(self):
        """Тест площади с большими числами"""
        self.assertEqual(area(100, 50), 2500)
    
    def test_area_small_numbers(self):
        """Тест площади с маленькими числами"""
        self.assertAlmostEqual(area(0.3, 0.4), 0.06)
    
    
    def test_perimeter_positive_integers(self):
        """Тест периметра с положительными целыми числами"""
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
    
    def test_perimeter_positive_floats(self):
        """Тест периметра с положительными дробными числами"""
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.5), 10.5)
        self.assertAlmostEqual(perimeter(1.2, 2.3, 3.4), 6.9)
    
    def test_perimeter_zero_sides(self):
        """Тест периметра с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(0, 5, 5), 10)
        self.assertEqual(perimeter(3, 0, 4), 7)
        self.assertEqual(perimeter(2, 3, 0), 5)
    
    def test_perimeter_large_numbers(self):
        """Тест периметра с большими числами"""
        self.assertEqual(perimeter(100, 150, 200), 450)
    
    def test_perimeter_small_numbers(self):
        """Тест периметра с маленькими числами"""
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.3), 0.6)
    
    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        self.assertEqual(perimeter(7, 7, 7), 21)
    
    def test_perimeter_isosceles(self):
        """Тест периметра равнобедренного треугольника"""
        self.assertEqual(perimeter(5, 5, 3), 13)
        self.assertEqual(perimeter(4, 6, 6), 16)
