from advent_of_code_2023.day_3.day_3 import sum_of_parts, create_1x1_box, extract_symbol_map


def test_sum_of_parts():
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert (4361, 467835) == sum_of_parts(data)


def test_create_1x1_box():
    result = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    assert result == create_1x1_box()


def test_extract_symbol_map():
    line_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split(
        "\n"
    )
    results = {(1, 3): "*", (3, 6): "#", (4, 3): "*", (5, 5): "+", (8, 3): "$", (8, 5): "*"}
    assert results == extract_symbol_map(line_data)
