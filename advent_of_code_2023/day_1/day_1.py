from advent_of_code_2023.common import get_data_from_file


def get_calibration_number(input_data):
    calibration_data = input_data.split("\n")
    calibration_values = [get_line_value(lv) for lv in calibration_data]
    return sum(calibration_values)


def get_line_value(line):
    filtered_value = [c for c in line if c.isdigit()]
    return int(filtered_value[0] + filtered_value[-1])


def replace_string_number(file_data):
    """Need to keep the first and last letter because they can be reused"""
    file_data = file_data.replace("one", "o1e")
    file_data = file_data.replace("two", "t2o")
    file_data = file_data.replace("three", "t3e")
    file_data = file_data.replace("four", "f4r")
    file_data = file_data.replace("five", "f5e")
    file_data = file_data.replace("six", "s6x")
    file_data = file_data.replace("seven", "s7n")
    file_data = file_data.replace("eight", "e8t")
    file_data = file_data.replace("nine", "n9e")

    return file_data


def main(filename, replace_string=None):
    file_data = get_data_from_file(filename)
    if replace_string:
        file_data = replace_string_number(file_data)
    calibration_number = get_calibration_number(file_data)
    print(f"Calibration number is {calibration_number}")


if __name__ in "__main__":
    main("day_1.txt")
    main("day_1.txt", True)
