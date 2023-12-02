from collections import defaultdict

import numpy as np

from advent_of_code_2023.common import get_data_from_file


def extract_game_data(line_data):
    subsets = [s.strip() for s in line_data.split(": ")[-1].strip().split(";")]
    game_data = defaultdict(int)
    for subset in subsets:
        subset_data = {}
        color_data = subset.split(", ")
        for color in color_data:
            value, name = color.split(" ")
            game_data[name] = max(game_data[name], int(value))
    return game_data


def get_sum_of_ids(data, function, constraints):
    line_data = data.split("\n")
    games_data = [extract_game_data(l) for l in line_data]
    game_ids = function(constraints, games_data)
    return sum(game_ids)


def get_game_ids_match_constraints(constraints, games_data):
    game_ids = []
    for idx, game_data in enumerate(games_data):
        if game_data.get("blue", 0) > constraints.get("blue", 0):
            continue
        if game_data.get("red", 0) > constraints.get("red", 0):
            continue
        if game_data.get("green", 0) > constraints.get("green", 0):
            continue
        game_ids.append(idx + 1)
    return game_ids


def get_game_product(constraints, games_data):
    game_products = []
    for idx, game_data in enumerate(games_data):
        calculate_product_by_game(game_data, game_products)
    return game_products


def calculate_product_by_game(game_data, game_products):
    values = np.array([_ for _ in game_data.values()])
    game_products.append(np.prod(values))


def main(filename, function, constraints):
    file_data = get_data_from_file(filename)
    sum_of_ids = get_sum_of_ids(file_data, function, constraints)
    print(f"Some of game IDs is {sum_of_ids}")


if __name__ in "__main__":
    main("day_2.txt", get_game_ids_match_constraints, {"red": 12, "blue": 14, "green": 13})
    main("day_2.txt", get_game_product, {})
