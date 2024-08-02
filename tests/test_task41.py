import cProfile
import pstats
import io
import pytest
from unittest.mock import patch
from task_44 import task41


def mock_input(prompt):
    return '3'


@patch('builtins.input', mock_input)
def test_оценка_по_числу():
    with patch('builtins.print') as mock_print:
        task41.оценка_по_числу()
        mock_print.assert_called_with("удовлетворительно")


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
