import cProfile
import pstats
import io
import pytest
from task_33 import task_11


def test_factorial():
    assert task_11.factorial(0) == 1
    assert task_11.factorial(1) == 1
    assert task_11.factorial(2) == 2
    assert task_11.factorial(3) == 6
    assert task_11.factorial(4) == 24
    assert task_11.factorial(5) == 120
    assert task_11.factorial(6) == 720
    assert task_11.factorial(10) == 3628800


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
