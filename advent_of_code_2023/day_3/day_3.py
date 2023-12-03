import itertools
import math
import re
from collections import defaultdict

from advent_of_code_2023.common import get_data_from_file


def create_1x1_box():
    return list(itertools.product((-1, 0, 1), (-1, 0, 1)))


def extract_symbol_map(line_data):
    return {
        (y, x): symbol
        for y, l in enumerate(line_data)
        for x, symbol in enumerate(l)
        if symbol != "." and not symbol.isdigit()
    }


def symbols_intersect_box(symbol_map, boundary_box):
    return symbol_map.keys() & boundary_box


def get_numbers_that_intersect_symbols(lines_data, symbol_map):
    box_1x1 = create_1x1_box()
    numbers_that_intersect = []
    for y, line_data in enumerate(lines_data):
        for match in re.finditer(r"\d+", line_data):
            number = int(match.group(0))
            boundary_box = create_boundary_box_around_match(box_1x1, match, y)
            if symbols_intersect_box(symbol_map, boundary_box):
                numbers_that_intersect.append(number)
    return numbers_that_intersect


def create_boundary_box_around_match(box_1x1, match, y):
    return {(y + b_y, x + b_x) for b_y, b_x in box_1x1 for x in range(match.start(), match.end())}


def get_symbols_by_numbers(lines_data, symbol_map):
    box_1x1 = create_1x1_box()
    numbers_by_symbol = defaultdict(list)
    for y, line_data in enumerate(lines_data):
        for match in re.finditer(r"\d+", line_data):
            number = int(match.group(0))
            boundary_box = create_boundary_box_around_match(box_1x1, match, y)
            if symbols_intersect_box(symbol_map, boundary_box):
                for symbol in symbol_map.keys() & boundary_box:
                    numbers_by_symbol[symbol].append(number)
    return numbers_by_symbol


def calculate_sum_of_products(symbols_by_number, symbol_map, symbol, occurence):
    values = sum(
        [math.prod(v) for k, v in symbols_by_number.items() if len(v) == occurence and symbol_map[k] == symbol]
    )
    return values


def sum_of_parts(data):
    lines_data = data.split("\n")
    symbol_map = extract_symbol_map(lines_data)
    numbers_that_intersect = get_numbers_that_intersect_symbols(lines_data, symbol_map)
    symbols_by_number = get_symbols_by_numbers(lines_data, symbol_map)
    sum_of_product = calculate_sum_of_products(symbols_by_number, symbol_map, "*", 2)
    return sum(numbers_that_intersect), sum_of_product


def main(filename):
    file_data = get_data_from_file(filename)
    sum_of_ids, sum_of_product = sum_of_parts(file_data)
    print(f"Some of parts is {sum_of_ids} ,  {sum_of_product}")


if __name__ in "__main__":
    main("day_3.txt")
