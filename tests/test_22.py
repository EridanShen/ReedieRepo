import cProfile
import pstats
import io
import pytest
from task22 import average_calculation

def test_calculate_average():
    assert average_calculation.calculate_average([1, 2, 3, 4, 5]) == 3
    assert average_calculation.calculate_average([10, 20, 30]) == 20
    assert average_calculation.calculate_average([5]) == 5

    with pytest.raises(ValueError):
        average_calculation.calculate_average([1, 2, 'a', 4])  # Тестируем нечисловой ввод


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
