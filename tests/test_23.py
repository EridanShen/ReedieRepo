import cProfile
import pstats
import io
import pytest
from task22 import rng_generator


def test_generate_random_number():
    assert 0 <= rng_generator.generate_random_number(0, 0) <= 0
    assert 1 <= rng_generator.generate_random_number(1, 1) <= 1
    assert 1 <= rng_generator.generate_random_number(1, 10) <= 10
    assert 0 <= rng_generator.generate_random_number(0, 100) <= 100

    with pytest.raises(ValueError):
        rng_generator.generate_random_number(-1, 10)

    with pytest.raises(ValueError):
        rng_generator.generate_random_number(10, 5)


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
