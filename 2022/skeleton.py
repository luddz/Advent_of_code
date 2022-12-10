import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

def part_1():
    return

def part_2():
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
    part_1()

    print("------------------------------------------------------------")
    print("Part 2")
    part_2()
