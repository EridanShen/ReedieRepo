import pytest
from unittest.mock import patch
from task_44 import task43
import cProfile


@patch('builtins.input', side_effect=['1', '1'])
@patch('builtins.print')
def test_следующая_дата(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "Следующая дата: 2.1"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['31', '1'])
@patch('builtins.print')
def test_end_of_month(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "Следующая дата: 1.2"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['28', '2'])
@patch('builtins.print')
def test_february(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "Следующая дата: 1.3"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['30', '4'])
@patch('builtins.print')
def test_end_of_april(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "Следующая дата: 1.5"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['31', '12'])
@patch('builtins.print')
def test_end_of_year(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "Следующая дата: 1.1"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['32', '1'])
@patch('builtins.print')
def test_invalid_day(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "ошибка"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['1', '13'])
@patch('builtins.print')
def test_invalid_month(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "ошибка"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['0', '1'])
@patch('builtins.print')
def test_invalid_day_zero(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "ошибка"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


@patch('builtins.input', side_effect=['1', '0'])
@patch('builtins.print')
def test_invalid_month_zero(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "ошибка"

    # Вызов функции с тестовыми данными
    task43.следующая_дата()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)


def run_profiling():
    # Примеры вызова функции
    print("Profile for следующая_дата:")
    for day in [1, 31, 28, 30]:
        for month in [1, 12, 2, 4]:
            print(task43.следующая_дата(day, month))


if __name__ == "__main__":
    pytest.main()
    cProfile.run('run_profiling()')
