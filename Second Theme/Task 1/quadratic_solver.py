import logging
import math

# Настройка логирования
logging.basicConfig(filename='quadratic_solver.log', level=logging.INFO, format='%(asctime)s %(message)s')

def solve_quadratic(a, b, c):
    try:
        logging.info(f'Initializing quadratic equation solving process with a={a}, b={b}, c={c}')
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("Discriminant in negative, no roots")
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        logging.info(f'Successfully solved: roots are {root1} and {root2}')
        return root1, root2
    except Exception as e:
        logging.error(f'Failed to solve quadratic equation: {e}')
        raise

# Пример использования
if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            roots = solve_quadratic(a, b, c)
            print(f"The roots of the quadratic equation are: {roots}")
            break
        except ValueError as e:
            print(e)
            print("Please try again with different coefficients.")
