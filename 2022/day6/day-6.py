import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines, dist_char=4):
    for line in input_lines:
        index = 0
        for i, l in enumerate(line):
            index += 1
            if len(set(line[i:i+dist_char])) == dist_char:
                index += dist_char - 1
                break
        print(f"{index = }")
    return

def part_2(input_lines):
    part_1(input_lines, 14)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e","--example", action='store_true')
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
