import pytest
from task_44 import task_calc
import cProfile
import pstats


def test_addition():
    assert task_calc.calculator(5, 3, '+') == 8


def test_subtraction():
    assert task_calc.calculator(5, 3, '-') == 2


def test_multiplication():
    assert task_calc.calculator(5, 3, '*') == 15


def test_division():
    assert task_calc.calculator(6, 3, '/') == 2.0


def test_division_by_zero():
    assert task_calc.calculator(6, 0, '/') == "Error: Division by zero"


def test_invalid_operation():
    assert task_calc.calculator(5, 3, '%') == "Error: Invalid operation"


def profile_calculator():
    cProfile.run('calculator(5, 3, "+")', 'profile_stats')

    # Печать профилирования
    with open('profile_stats', 'r') as f:
        stats = pstats.Stats('profile_stats')
        stats.sort_stats('cumulative')  # Можно сортировать по времени выполнения
        stats.print_stats()


if __name__ == "__main__":
    pytest.main()
