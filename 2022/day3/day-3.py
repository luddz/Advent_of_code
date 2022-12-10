import argparse
from enum import Enum
from dataclasses import dataclass
import string

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines):
    priority_sum = 0
    alphaBet = string.ascii_lowercase + string.ascii_uppercase
    for line in input_lines:
        l = line.strip()
        mid = len(l)//2
        comp1, comp2 = l[:mid], l[mid:]
        miss_placed = ''
        for p in comp1:
            if p in comp2:
                miss_placed = p
                break
        priority_sum += alphaBet.find(miss_placed) + 1
    
    print(f"{priority_sum = }")

def part_2(input_lines):
    priority_sum = 0
    alphaBet = string.ascii_lowercase + string.ascii_uppercase
    three_lines = iter(input_lines)
    for l1, l2, l3 in zip(three_lines, three_lines, three_lines):
        _l1 = l1.strip()
        _l2 = l2.strip()
        _l3 = l3.strip()
        auth_token = ''
        for a in _l1:
            if a in _l2 and a in _l3:
                auth_token = a
                break
        priority_sum += alphaBet.find(auth_token) + 1
    
    print(f"{priority_sum = }")
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
