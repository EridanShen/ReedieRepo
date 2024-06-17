import math

def square_perimeter(a):
    return 4 * a

def square_area(a):
    return a ** 2

def rectangle_area_and_perimeter(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

def circle_length(d):
    return math.pi * d

def cube_volume_and_surface_area(a):
    volume = a ** 3
    surface_area = 6 * (a ** 2)
    return volume, surface_area

def rectangular_parallelepiped_volume_and_surface_area(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area

def circle_length_and_area(R):
    length = 2 * math.pi * R
    area = math.pi * (R ** 2)
    return length, area

def arithmetic_mean(a, b):
    return (a + b) / 2

def geometric_mean(a, b):
    return math.sqrt(a * b)

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

print("Периметр квадрата:", square_perimeter(a))
print("Площадь квадрата", square_area(a))
print("Площадь и периметр прямоугольника", rectangle_area_and_perimeter(a, b))
print("Длина окружности", circle_length(d))
print("Объем и площадь поверхности куба", cube_volume_and_surface_area(a))
print("Объем и площадь поверхности параллелепипеда", rectangular_parallelepiped_volume_and_surface_area(a, b, c))
print("Длина окружности и площадь круга", circle_length_and_area(R))
print("Среднее арифметическое:", arithmetic_mean(a, b))
print("Среднее геометрическое", geometric_mean(a, b))
print("Сумма, разность, произведение и частное квадратов", sum_difference_product_quotient_of_squares(a, b))