from collections import defaultdict

from advent_of_code_2023.common import get_data_from_file


def calculate_game_card_score(card_data):
    having_numbers_string, winning_numbers_string = card_data.split(" | ")
    having_numbers = extract_set_of_numbers(having_numbers_string)
    winning_numbers = extract_set_of_numbers(winning_numbers_string)
    matching_numbers = len(having_numbers & winning_numbers)

    return 2 ** (matching_numbers - 1) if matching_numbers > 0 else 0


def calculate_sum_of_pile_score(data):
    card_data = data.split("\n")
    scores = [calculate_game_card_score(cd.split(": ")[1].strip()) for cd in card_data]
    return sum(scores)


def calculate_number_of_cards(data):
    card_data = data.split("\n")
    cards = defaultdict(int)
    for idx, card in enumerate(card_data):
        calculate_new_cards_won(card, cards, idx)
    return sum(cards.values())


def calculate_new_cards_won(card, cards, idx):
    cards[idx] += 1
    having_numbers_string, winning_numbers_string = card.split(": ")[1].strip().split(" | ")
    having_numbers = extract_set_of_numbers(having_numbers_string)
    winning_numbers = extract_set_of_numbers(winning_numbers_string)
    matching_numbers = len(having_numbers & winning_numbers)
    for new_card_idx in range(matching_numbers):
        cards[idx + 1 + new_card_idx] += cards[idx]


def extract_set_of_numbers(having_numbers_string):
    return set([int(n) for n in having_numbers_string.split()])


def main(filename):
    file_data = get_data_from_file(filename)
    points = calculate_sum_of_pile_score(file_data)
    cards = calculate_number_of_cards(file_data)
    print(f"Number of {points} pts, cards {cards}")


if __name__ in "__main__":
    main("day_4.txt")
