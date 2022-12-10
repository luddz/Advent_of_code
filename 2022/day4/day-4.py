import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines):
    def check_range_subset(r1, r2):
        return r2[0] <= r1[0] and r1[-1] <= r2[-1] 

    number_subsets = 0
    for line in input_lines:
        l = line.strip().split(",")
        s, s1 = l[0], l[1]
        r1 = [int(r) for r in s.split('-')]
        r2 = [int(r) for r in s1.split('-')]
        if check_range_subset(r1, r2) or check_range_subset(r2, r1):
            number_subsets += 1
    print(f"{number_subsets = }")
    return

def part_2(input_lines):
    not_overlapping = 0
    def check_range_not_overlaping(r1, r2):
        return r1[-1] < r2[0] or r1[0] > r2[-1]

    for line in input_lines:
        l = line.strip().split(",")
        s, s1 = l[0], l[1]
        r1 = [int(r) for r in s.split('-')]
        r2 = [int(r) for r in s1.split('-')]
        if check_range_not_overlaping(r1, r2):
            not_overlapping += 1

    print(f"overlap: {len(input_lines) - not_overlapping}")
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e","--example", action='store_true')
    args = parser.parse_args()

    input_lines = []
    file = test_input if not args.example else example_input
    with open(file, 'r') as f:
        input_lines = f.readlines()
    
    print("------------------------------------------------------------")
    print("Part 1")
    part_1(input_lines)

    print("------------------------------------------------------------")
    print("Part 2")
    part_2(input_lines)
