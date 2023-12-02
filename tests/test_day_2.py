from advent_of_code_2023.day_2.day_2 import get_sum_of_ids, get_game_ids_match_constraints, get_game_product


def test_sum_of_ids():
    data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    constraints = {"red": 12, "blue": 14, "green": 13}
    sum_of_ids = get_sum_of_ids(data, get_game_ids_match_constraints, constraints)
    assert 8 == sum_of_ids


def test_sum_of_ids_part_2():
    data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    constraints = {}
    sum_of_ids = get_sum_of_ids(data, get_game_product, constraints)
    assert 2286 == sum_of_ids
