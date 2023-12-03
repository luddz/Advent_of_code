import argparse
from enum import Enum
from dataclasses import dataclass
import string

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines):
    calibration_values = []
    nums = [str(i) for i in range(10)]
    for line in input_lines:
        first_num = None
        last_num = None
        for c in line:
            if c in nums:
                if first_num is None:
                    first_num = c
                else:
                    last_num = c
        if last_num is None:
            last_num = first_num
        number = first_num + last_num
        calibration_values.append(int(number))
    return sum(calibration_values)


from dataclasses import dataclass

@dataclass
class num_string_repr:
    value: int
    literal: str
    small_index: int
    max_index: int

    def get_largest_index(self) -> int | None:
        return self.max_index

    def get_small_index(self) -> int | None:
        return self.small_index


def find_smallest_index(n:num_string_repr, line: str):
    ls = line.find(n.literal)
    ls = ls if ls >= 0 else None
    ns = line.find(str(n.value))
    ns = ns if ns >= 0 else None
    if ls is not None and ns is not None:
        return min(ls, ns)
    if ls is None and ns is not None:
        return ns 
    if ls is not None and ns is None:
        return ls 
    return None


def find_largest_index(n:num_string_repr, line: str):
    ls = line.rfind(n.literal)
    ls = ls if ls >= 0 else None
    ns = line.rfind(str(n.value))
    ns = ns if ns >= 0 else None
    if ls is not None and ns is not None:
        return max(ls, ns)
    if ls is None and ns is not None:
        return ns 
    if ls is not None and ns is None:
        return ls 
    return None


def part_2(input_lines):
    calibration_values = []
    nums = [i for i in range(1,10)]
    liternal_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in input_lines:
        numbers = [num_string_repr(i, j, None, None) for i,j in zip(nums, liternal_nums)]
        for n in numbers:
            n.small_index = find_smallest_index(n, line)
            n.max_index = find_largest_index(n, line)

        min_start_index = None
        max_start_index = None
        for n in numbers:
            if n.small_index is None:
                continue
            if min_start_index is None:
                min_start_index = n
            if max_start_index is None:
                max_start_index = n

            if n.small_index < min_start_index.small_index:
                min_start_index = n
            
            if n.max_index > max_start_index.max_index:
                max_start_index = n

        number = str(min_start_index.value) + str(max_start_index.value)
        print(number)
        calibration_values.append(int(number))
    return sum(calibration_values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e","--example", action='store_true')
    args = parser.parse_args()

    input_lines = []
    file = test_input if not args.example else example_input
    with open(file, 'r') as f:
        input_lines = [l.strip() for l in f.readlines() if len(l) > 0]
    
    print("------------------------------------------------------------")
    print("Part 1")
    res = part_1(input_lines)
    print(f"Result part 1: { res}")
    print("------------------------------------------------------------")
    print("Part 2")
    res2 = part_2(input_lines)
    print(f"Result part 2: { res2}")

