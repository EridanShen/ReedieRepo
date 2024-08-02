import math


def solve_quadratic(a, b, c):
    try:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("Discriminant in negative, no roots")
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    except Exception as e:
        raise

