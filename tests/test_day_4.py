from advent_of_code_2023.day_4.day_4 import (
    calculate_game_card_score,
    calculate_sum_of_pile_score,
    calculate_number_of_cards,
)


def test_calculate_game_card_score():
    data = """41 48 83 86 17 | 83 86  6 31 17  9 48 53"""
    assert 8 == calculate_game_card_score(data)
    data = """13 32 20 16 61 | 61 30 68 82 17 32 24 19"""
    assert 2 == calculate_game_card_score(data)
    data = """1 21 53 59 44 | 69 82 63 72 16 21 14  1"""
    assert 2 == calculate_game_card_score(data)
    data = """41 92 73 84 69 | 59 84 76 51 58  5 54 83"""
    assert 1 == calculate_game_card_score(data)
    data = """87 83 26 28 32 | 88 30 70 12 93 22 82 36"""
    assert 0 == calculate_game_card_score(data)
    data = """31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    assert 0 == calculate_game_card_score(data)


def test_calculate_sum_of_pile_score():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    assert 13 == calculate_sum_of_pile_score(data)


def test_calculate_number_of_cards():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    assert 30 == calculate_number_of_cards(data)
