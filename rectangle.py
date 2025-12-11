import unittest

def area(a, b):
    """
    Возвращает площадь прямоугольника.
    
    Параметры:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника
    
    Возвращаемое значение:
        area (float): площадь прямоугольника
    """
    return a * b

def perimeter(a, b):
    """
    Возвращает периметр прямоугольника.
    
    Параметры:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника
    
    Возвращаемое значение:
        perimeter (float): периметр прямоугольника
    """
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_positive_integers(self):
        """Тест площади с положительными целыми числами"""
        self.assertEqual(area(5, 4), 20)
        self.assertEqual(area(3, 7), 21)
    
    def test_area_positive_floats(self):
        """Тест площади с положительными дробными числами"""
        self.assertAlmostEqual(area(2.5, 3.5), 8.75)
        self.assertAlmostEqual(area(1.2, 2.3), 2.76)
    
    def test_area_square(self):
        """Тест площади квадрата (частный случай прямоугольника)"""
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(5, 5), 25)
    
    def test_area_zero(self):
        """Тест площади с нулевыми сторонами"""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_large_numbers(self):
        """Тест площади с большими числами"""
        self.assertEqual(area(1000, 500), 500000)
    
    def test_perimeter_positive_integers(self):
        """Тест периметра с положительными целыми числами"""
        self.assertEqual(perimeter(5, 4), 18)
        self.assertEqual(perimeter(3, 7), 20)
    
    def test_perimeter_positive_floats(self):
        """Тест периметра с положительными дробными числами"""
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)
        self.assertAlmostEqual(perimeter(1.2, 2.3), 7.0)
    
    def test_perimeter_square(self):
        """Тест периметра квадрата (частный случай прямоугольника)"""
        self.assertEqual(perimeter(10, 10), 40)
        self.assertEqual(perimeter(5, 5), 20)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)
    
    def test_perimeter_large_numbers(self):
        """Тест периметра с большими числами"""
        self.assertEqual(perimeter(1000, 500), 3000)
    
    def test_perimeter_small_numbers(self):
        """Тест периметра с маленькими числами"""
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6)

if __name__ == "__main__":
    unittest.main()