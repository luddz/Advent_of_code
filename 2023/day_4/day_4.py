import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"


def part_1(input_lines):

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
    return


def part_2(input_lines):
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
