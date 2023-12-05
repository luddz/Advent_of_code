import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"


def part_1(input_lines: list[str]) -> None:
    total_score = 0
    for line in input_lines:
        card, numbers = line.split(":")
        n1, n2 = numbers.split("|")
        winning_numbers = [*filter(None, n1.split(" "))]
        players_numbers = [*filter(None, n2.split(" "))]
        correct = -1  # Start at -1 due to score is 2^correct
        for n in players_numbers:
            if n in winning_numbers:
                correct += 1

        card_score = 2**correct if correct >= 0 else 0
        print(f"{card = } - {card_score = }")
        total_score += card_score
    print(f"{total_score = }")


def num_wins(l1, l2):
    return len([l_ for l_ in l1 if l_ in l2])


def inner_recursion(cards, start_index):
    c = cards[start_index]
    wins = num_wins(c[0], c[1])
    if wins == 0:
        return 1
    sub_cards = 0
    for i in range(wins):
        sub_cards += inner_recursion(cards, start_index + i + 1)
    return sub_cards + 1


def part_2(input_lines: list[str]) -> None:
    cards = []
    for line in input_lines:
        card, numbers = line.split(":")
        n1, n2 = numbers.split("|")
        cards.append(([*filter(None, n1.split(" "))], [*filter(None, n2.split(" "))]))
    total_cards = 0
    for idx in range(len(cards)): 
        total_cards += inner_recursion(cards, idx)

    print(f"{total_cards = }")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e", "--example", action='store_true')
    args = parser.parse_args()

    input_lines = []
    file = test_input if not args.example else example_input
    with open(file, 'r') as f:
        input_lines = [l.strip() for l in f.readlines()]
    
    print("------------------------------------------------------------")
    print("Part 1")
    part_1(input_lines)

    print("------------------------------------------------------------")
    print("Part 2")
    part_2(input_lines)
