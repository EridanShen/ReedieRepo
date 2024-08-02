import cProfile
import pstats
import io
import pytest
from task_33 import task8


def test_is_prime():
    assert task8.is_prime(2) == True
    assert task8.is_prime(3) == True
    assert task8.is_prime(4) == False
    assert task8.is_prime(5) == True
    assert task8.is_prime(10) == False
    assert task8.is_prime(29) == True
    assert task8.is_prime(50) == False
    assert task8.is_prime(97) == True
    assert task8.is_prime(1) == False
    assert task8.is_prime(0) == False
    assert task8.is_prime(-3) == False


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
