from task11 import task2
import pytest
import cProfile
import pstats
import io


def test_full_meters():
    assert task2.full_meters(250) == 2
    assert task2.full_meters(1234) == 12


def test_full_tons():
    assert task2.full_tons(1500) == 1
    assert task2.full_tons(5000) == 5


def test_full_kilobytes():
    assert task2.full_kilobytes(2048) == 2
    assert task2.full_kilobytes(1023) == 0


def test_max_segments():
    assert task2.max_segments(10, 3) == 3
    assert task2.max_segments(25, 5) == 5
    with pytest.raises(ValueError):
        task2.max_segments(-10, 3)
    with pytest.raises(ValueError):
        task2.max_segments(10, 0)


def test_remaining_length():
    assert task2.remaining_length(10, 3) == 1
    assert task2.remaining_length(25, 5) == 0
    with pytest.raises(ValueError):
        task2.remaining_length(-10, 3)
    with pytest.raises(ValueError):
        task2.remaining_length(10, 0)


def test_left_and_right_digits():
    assert task2.left_and_right_digits(23) == (2, 3)
    assert task2.left_and_right_digits(99) == (9, 9)
    with pytest.raises(ValueError):
        task2.left_and_right_digits(5)
    with pytest.raises(ValueError):
        task2.left_and_right_digits(123)


def test_sum_and_product_of_digits():
    assert task2.sum_and_product_of_digits(23) == (5, 6)
    assert task2.sum_and_product_of_digits(99) == (18, 81)
    with pytest.raises(ValueError):
        task2.sum_and_product_of_digits(5)
    with pytest.raises(ValueError):
        task2.sum_and_product_of_digits(123)


def test_reversed_digits():
    assert task2.reversed_digits(23) == 32
    assert task2.reversed_digits(99) == 99
    with pytest.raises(ValueError):
        task2.reversed_digits(5)
    with pytest.raises(ValueError):
        task2.reversed_digits(123)


def test_first_digit_of_three_digit():
    assert task2.first_digit_of_three_digit(123) == 1
    assert task2.first_digit_of_three_digit(987) == 9
    with pytest.raises(ValueError):
        task2.first_digit_of_three_digit(99)
    with pytest.raises(ValueError):
        task2.first_digit_of_three_digit(1000)


def test_last_and_middle_digits():
    assert task2.last_and_middle_digits(123) == (3, 2)
    assert task2.last_and_middle_digits(987) == (7, 8)
    with pytest.raises(ValueError):
        task2.last_and_middle_digits(99)
    with pytest.raises(ValueError):
        task2.last_and_middle_digits(1000)


if __name__ == "__main__":
    pytest.main()
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
