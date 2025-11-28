import unittest

def area(a):
    """
    Возвращает площадь квадрата.
    
    Параметры:
        a (float): сторона квадрата
    
    Возвращаемое значение:
        area (float): площадь квадрата
    """
    return a * a

def perimeter(a):
    """
    Возвращает периметр квадрата.
    
    Параметры:
        a (float): сторона квадрата
    
    Возвращаемое значение:
        perimeter (float): периметр квадрата
    """
    return 4 * a

class SquareTestCase(unittest.TestCase):
    """
    Тесты для функций площади и периметра квадрата
    """
    
    
    def test_area_positive_integer(self):
        """Тест площади с положительным целым числом"""
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
    
    def test_area_positive_float(self):
        """Тест площади с положительным дробным числом"""
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(area(1.2), 1.44)
    
    def test_area_zero(self):
        """Тест площади с нулевой стороной"""
        self.assertEqual(area(0), 0)
    
    def test_area_large_number(self):
        """Тест площади с большим числом"""
        self.assertEqual(area(1000), 1000000)
    
    def test_area_small_number(self):
        """Тест площади с маленьким числом"""
        self.assertAlmostEqual(area(0.1), 0.01)
    
    def test_perimeter_positive_integer(self):
        """Тест периметра с положительным целым числом"""
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
    
    def test_perimeter_positive_float(self):
        """Тест периметра с положительным дробным числом"""
        self.assertAlmostEqual(perimeter(2.5), 10.0)
        self.assertAlmostEqual(perimeter(1.2), 4.8)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевой стороной"""
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_large_number(self):
        """Тест периметра с большим числом"""
        self.assertEqual(perimeter(1000), 4000)
    
    def test_perimeter_small_number(self):
        """Тест периметра с маленьким числом"""
        self.assertAlmostEqual(perimeter(0.1), 0.4)