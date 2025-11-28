# Unit Tests for Geometric Library

## Project Description

Проект содержит unit-тесты для библиотеки геометрических вычислений. Тесты разработаны с использованием фреймворка `unittest` и покрывают основные функции вычисления площадей и периметров геометрических фигур.

## Project Structure

- `rectangle.py` - tests for rectangle
- `circle.py` - tests for circle  
- `square.py` - tests for square
- `triangle.py` - tests for triangle
- `README.md` - documentation
- `documentation.md` - solve description

## Tested Functions

### Rectangle
- `area(a, b)` - rectangle area
- `perimeter(a, b)` - rectangle perimeter

### Circle
- `area(r)` - circle area
- `perimeter(r)` - circle circumference

### Square
- `area(a)` - square area
- `perimeter(a)` - square perimeter

### Triangle
- `area(a, h)` - triangle area
- `perimeter(a, b, c)` - triangle perimeter

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Running Tests

- python3 -m unittest rectangle.py -v
- python3 -m unittest circle.py -v
- python3 -m unittest square.py -v
- python3 -m unittest triangle.py -v

### All Tests
```bash
python3 -m unittest discover -v