import cProfile
import pytest
from unittest.mock import patch
from task_44 import task45  # Замените на правильный импорт


@patch('builtins.input', side_effect=['123'])
@patch('builtins.print')
def test_number_123(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "сто двадцать три"

    # Вызов функции с тестовыми данными
    task45.описание_числа()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['999'])
@patch('builtins.print')
def test_number_999(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "девятьсот девяносто девять"

    # Вызов функции с тестовыми данными
    task45.описание_числа()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['105'])
@patch('builtins.print')
def test_number_105(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "сто пять"

    # Вызов функции с тестовыми данными
    task45.описание_числа()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['50'])
@patch('builtins.print')
def test_invalid_number(mock_print, mock_input):
    # Ожидаемый результат
    expected_output = "ошибка"

    # Вызов функции с тестовыми данными
    task45.описание_числа()

    # Проверка вызова print
    mock_print.assert_called_with(expected_output)

if __name__ == "__main__":
    pytest.main()



# Функция для запуска и профилирования
def run_profiling():
    with patch('builtins.input', side_effect=['123']):
        task45.описание_числа()


def profile_function():
    # Создаем объект профайлера и запускаем профилирование
    profiler = cProfile.Profile()
    profiler.enable()

    run_profiling()  # Запускаем функцию, которую нужно профилировать

    profiler.disable()
    profiler.dump_stats('profile_output.prof')  # Сохраняем результаты в файл


def test_profiling():
    # Запускаем профилирование
    profile_function()

    # Проверяем, что файл профилирования был создан
    import os
    assert os.path.exists('profile_output.prof')
