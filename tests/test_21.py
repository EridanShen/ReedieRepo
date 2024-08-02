import cProfile
import pstats
import io
import pytest
from task22 import quadratic_solver


def test_solve_quadratic():
    # Test case 1: Two distinct real roots
    assert quadratic_solver.solve_quadratic(1, -3, 2) == (2, 1)

    # Test case 2: One real root (repeated root)
    assert quadratic_solver.solve_quadratic(1, -2, 1) == (1, 1)

    # Test case 3: No real roots (negative discriminant)
    with pytest.raises(ValueError, match="Discriminant in negative, no roots"):
        quadratic_solver.solve_quadratic(1, 0, 2)


def run_tests():
    pytest.main()


if __name__ == "__main__":
    # Создаем объект профайлера
    profiler = cProfile.Profile()
    profiler.enable()  # Начинаем профилирование

    run_tests()

    profiler.disable()  # Останавливаем профилирование

    # Сохраняем результаты в объекте StringIO
    s = io.StringIO()
    sort_by = 'cumulative'
    ps = pstats.Stats(profiler, stream=s).sort_stats(sort_by)
    ps.print_stats()

    # Выводим результаты
    with open('profiling_results.txt', 'w') as f:
        f.write(s.getvalue())

