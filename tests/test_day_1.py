from advent_of_code_2023.day_1.day_1 import get_calibration_number, get_line_value, replace_string_number


def test_get_line_value():
    data = "1abc2"
    line_value = get_line_value(data)
    assert line_value == 12

    data = "pqr3stu8vwx"
    line_value = get_line_value(data)
    assert line_value == 38

    data = "a1b2c3d4e5f"
    line_value = get_line_value(data)
    assert line_value == 15

    data = "treb7uchet"
    line_value = get_line_value(data)
    assert line_value == 77


def test_get_calibration_number():
    data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    calibration_number = get_calibration_number(data)
    assert calibration_number == 142


def test_get_calibration_number_with_replace():
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    filtered_data = replace_string_number(data)
    calibration_number = get_calibration_number(filtered_data)
    assert calibration_number == 281
