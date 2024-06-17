import math

# Дана сторона квадрата a. Найти его периметр P = 4·a
def square_perimeter(a):
    return 4 * a

# Дана сторона квадрата a. Найти его площадь S = a^2
def square_area(a):
    return a ** 2

# Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
def rectangle_area_and_perimeter(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

# Дан диаметр окружности d. Найти её длину L = π·d, π = 3.14
def circle_length(d):
    return math.pi * d

# Дана длина ребра куба a. Найти объем куба V = a^3 и площадь его поверхности S = 6·a^2
def cube_volume_and_surface_area(a):
    volume = a ** 3
    surface_area = 6 * (a ** 2)
    return volume, surface_area

# Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)
def rectangular_parallelepiped_volume_and_surface_area(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area

# Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R^2, π=3.14
def circle_length_and_area(R, pi=3.14):
    length = 2 * pi * R
    area = pi * (R ** 2)
    return length, area

# Даны два числа a и b. Найти их среднее арифметическое: (a + b) / 2
def arithmetic_mean(a, b):
    return (a + b) / 2

# Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a·b)^1/2
def geometric_mean(a, b):
    return math.sqrt(a * b)

# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
def sum_difference_product_quotient_of_squares(a, b):
    sum_ab = a + b
    difference_ab = a - b
    product_ab = a * b
    quotient_of_squares = (a ** 2) / (b ** 2)
    return sum_ab, difference_ab, product_ab, quotient_of_squares

# Примеры использования функций
a = 5
b = 10
c = 3
d = 8
R = 7

print("Периметр квадрата со стороной a:", square_perimeter(a))
print("Площадь квадрата со стороной a:", square_area(a))
print("Площадь и периметр прямоугольника с сторонами a и b:", rectangle_area_and_perimeter(a, b))
print("Длина окружности с диаметром d:", circle_length(d))
print("Объем и площадь поверхности куба с ребром a:", cube_volume_and_surface_area(a))
print("Объем и площадь поверхности прямоугольного параллелепипеда с ребрами a, b и c:", rectangular_parallelepiped_volume_and_surface_area(a, b, c))
print("Длина окружности и площадь круга с радиусом R:", circle_length_and_area(R))
print("Среднее арифметическое чисел a и b:", arithmetic_mean(a, b))
print("Среднее геометрическое неотрицательных чисел a и b:", geometric_mean(a, b))
print("Сумма, разность, произведение и частное квадратов ненулевых чисел a и b:", sum_difference_product_quotient_of_squares(a, b))