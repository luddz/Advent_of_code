import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines):
    possible_game_ids = []
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in input_lines:
        game, draws = line.split(":")
        reasonable = True
        for draw in draws.split(";"):
            for d in draw.split(","):
                num, color = d.strip().split(" ")
                if limits[color] < int(num):
                    reasonable = False
        if reasonable:
            possible_game_ids.append(int(game.split(" ")[1]))
    print(f"Result: {sum(possible_game_ids)}")


def part_2(input_lines):
    min_num_cubes_per_game = []
    for line in input_lines:
        min_pos_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
        }
        _, draws = line.split(":")
        for draw in draws.split(";"):
            for d in draw.split(","):
                num, color = d.strip().split(" ")
                min_pos_cubes[color] = max(min_pos_cubes[color], int(num))
        min_num_cubes_per_game.append(min_pos_cubes)
    
    res = sum([g["red"] * g["blue"] * g["green"] for g in min_num_cubes_per_game])
    print(f"Result: {res}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e","--example", action='store_true')
    args = parser.parse_args()

    input_lines = []
    file = test_input if not args.example else example_input
    with open(file, 'r') as f:
        input_lines = [li.strip() for li in f.readlines() if len(li) > 0]
    
    print("------------------------------------------------------------")
    print("Part 1")
    part_1(input_lines)

    print("------------------------------------------------------------")
    print("Part 2")
    part_2(input_lines)
