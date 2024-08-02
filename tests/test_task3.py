from task11 import task3
import pytest
import cProfile
import pstats
import io


def test_is_positive():
    assert task3.is_positive(5) == True
    assert task3.is_positive(-1) == False
    assert task3.is_positive(0) == False


def test_is_odd():
    assert task3.is_odd(5) == True
    assert task3.is_odd(4) == False
    assert task3.is_odd(0) == False


def test_is_even():
    assert task3.is_even(4) == True
    assert task3.is_even(5) == False
    assert task3.is_even(0) == True


def test_inequalities_A_gt_2_and_B_le_3():
    assert task3.inequalities_A_gt_2_and_B_le_3(3, 3) == True
    assert task3.inequalities_A_gt_2_and_B_le_3(2, 3) == False
    assert task3.inequalities_A_gt_2_and_B_le_3(3, 4) == False


def test_inequalities_A_ge_0_or_B_lt_minus_2():
    assert task3.inequalities_A_ge_0_or_B_lt_minus_2(0, -3) == True
    assert task3.inequalities_A_ge_0_or_B_lt_minus_2(-1, -3) == True
    assert task3.inequalities_A_ge_0_or_B_lt_minus_2(-1, -2) == False


def test_double_inequality_A_lt_B_lt_C():
    assert task3.double_inequality_A_lt_B_lt_C(1, 2, 3) == True
    assert task3.double_inequality_A_lt_B_lt_C(1, 3, 2) == False
    assert task3.double_inequality_A_lt_B_lt_C(3, 2, 1) == False


def test_B_between_A_and_C():
    assert task3.B_between_A_and_C(1, 2, 3) == True
    assert task3.B_between_A_and_C(3, 2, 1) == True
    assert task3.B_between_A_and_C(2, 3, 1) == False


def test_both_A_and_B_odd():
    assert task3.both_A_and_B_odd(1, 3) == True
    assert task3.both_A_and_B_odd(2, 3) == False
    assert task3.both_A_and_B_odd(1, 2) == False


def test_at_least_one_odd():
    assert task3.at_least_one_odd(1, 3) == True
    assert task3.at_least_one_odd(2, 3) == True
    assert task3.at_least_one_odd(2, 4) == False


def test_exactly_one_odd():
    assert task3.exactly_one_odd(1, 3) == False
    assert task3.exactly_one_odd(2, 3) == True
    assert task3.exactly_one_odd(2, 4) == False


if __name__ == "__main__":
    pytest.main()
    # Создаем объект профайлера
    profiler = cProfile.Profile()
    profiler.enable()  # Начинаем профилирование

    profiler.disable()  # Останавливаем профилирование

    # Сохраняем результаты в объекте StringIO
    s = io.StringIO()
    sort_by = 'cumulative'
    ps = pstats.Stats(profiler, stream=s).sort_stats(sort_by)
    ps.print_stats()

    # Выводим результаты
    print(s.getvalue())
