import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines):
    calibration_values = []
    nums = [str(i) for i in range(10)]	
    print(nums)
    for line in input_lines:
        print(line)
        first_num = None
        last_num = None
        for c in line:
            if c in nums:
                print(c)
                if first_num is None:
                    first_num = c
                else:
                    last_num = c
            if last_num is None:
                last_num = first_num
        number = first_num + last_num
        calibration_values.append(int(number))
    return sum(calibration_values)


def part_2(input_lines):
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
    res = part_1(input_lines)
    print(f"Result part 1: { res}")
    print("------------------------------------------------------------")
    print("Part 2")
    part_2(input_lines)
