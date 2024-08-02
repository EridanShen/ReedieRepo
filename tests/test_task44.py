import pytest
from unittest.mock import patch
from task_44 import task44
import cProfile
import pstats


@patch('builtins.input', side_effect=['С', '1'])
@patch('builtins.print')
def test_turn_right(mock_print, mock_input):
    expected_output = "Новое направление: В"
    task44.направление_робота()
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['С', '-1'])
@patch('builtins.print')
def test_turn_left(mock_print, mock_input):
    expected_output = "Новое направление: З"
    task44.направление_робота()
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['С', '0'])
@patch('builtins.print')
def test_no_turn(mock_print, mock_input):
    expected_output = "Новое направление: С"
    task44.направление_робота()
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['X', '1'])
@patch('builtins.print')
def test_invalid_direction(mock_print, mock_input):
    expected_output = "ошибка направления"
    task44.направление_робота()
    mock_print.assert_called_with(expected_output)

@patch('builtins.input', side_effect=['С', '2'])
@patch('builtins.print')
def test_invalid_command(mock_print, mock_input):
    expected_output = "ошибка команды"
    task44.направление_робота()
    mock_print.assert_called_with(expected_output)


def run_tests():
    pytest.main()


if __name__ == "__main__":
    pytest.main()
    profiler = cProfile.Profile()
    profiler.enable()
    run_tests()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
