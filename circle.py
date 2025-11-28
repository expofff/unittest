import math
import unittest

def area(r):
    """
    Возвращает площадь круга.
    
    Параметры:
        r (float): радиус круга
    
    Возвращаемое значение:
        area (float): площадь круга
    """
    return math.pi * r * r

def perimeter(r):
    """
    Возвращает длину окружности (периметр круга).
    
    Параметры:
        r (float): радиус круга
    
    Возвращаемое значение:
        perimeter (float): длина окружности
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    """
    Тесты для функций площади и периметра круга
    """
    
    def test_area_positive_integer(self):
        """Тест площади с положительным целым радиусом"""
        self.assertAlmostEqual(area(5), math.pi * 25)
    
    def test_area_positive_float(self):
        """Тест площади с положительным дробным радиусом"""
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)
    
    def test_area_zero(self):
        """Тест площади с нулевым радиусом"""
        self.assertEqual(area(0), 0)
    
    def test_area_large_number(self):
        """Тест площади с большим радиусом"""
        self.assertAlmostEqual(area(100), math.pi * 10000)
    
    def test_area_small_number(self):
        """Тест площади с маленьким радиусом"""
        self.assertAlmostEqual(area(0.1), math.pi * 0.01)
    

    def test_perimeter_positive_integer(self):
        """Тест периметра с положительным целым радиусом"""
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)
    
    def test_perimeter_positive_float(self):
        """Тест периметра с положительным дробным радиусом"""
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевым радиусом"""
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_large_number(self):
        """Тест периметра с большим радиусом"""
        self.assertAlmostEqual(perimeter(100), 2 * math.pi * 100)
    
    def test_perimeter_small_number(self):
        """Тест периметра с маленьким радиусом"""
        self.assertAlmostEqual(perimeter(0.1), 2 * math.pi * 0.1)