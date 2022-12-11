import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

@dataclass
class Bay:
    stack: list

def create_crates_example():
    b1 = Bay(['Z','N'])
    b2 = Bay(['M','C','D'])
    b3 = Bay(['P'])
    return [b1,b2,b3]


def create_crates_test():
    return [
        Bay(["W", "M", "L", "F"]),
        Bay(["B", "Z","V","M","F"]),
        Bay(["H","V","R","S","L","Q"]),
        Bay(["F","S","V","Q","p","M","T","J"]),
        Bay(["L","S","W"]),
        Bay(["F","V","P","M","R","J","W"]),
        Bay(["J","Q","C","P","N","R","F"]),
        Bay(["V","H","P","S","Z","W","R","B"]),
        Bay(["B","M","J","C","G","H","Z","W"]),
    ]

def part_1(input_lines, part_2 = False):
    cargo_bay = create_crates_test() if not args.example else  create_crates_example()
    def move(num, _from, _to):
        from_s = cargo_bay[_from - 1].stack
        cargo_bay[_from - 1].stack = from_s[:-num]
        t = from_s[-num:]
        t = t if part_2 else t[::-1]
        cargo_bay[_to - 1].stack.extend(t) # Add in reverse order

    def parse_move(line):
        a = line[len("move"):].split(" from ")
        _move = int(a[0])
        a = a[1].split(" to ")
        return _move, int(a[0]), int(a[1])

    c = 10 if not args.example else 5
    for line in input_lines[c:]:
        line =  line.replace("\n", "")
        num, _f, _t = parse_move(line)
        move(num, _f, _t)

    res = ""
    for b in cargo_bay:
        res += b.stack[-1]
    
    print(res)
    return

def part_2(input_lines):
    part_1(input_lines, True)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e","--example", action='store_true')
    args = parser.parse_args()

    input_lines = []
    file = test_input if not args.example else example_input
    with open(file, 'r') as f:
        input_lines = [l for l in f.readlines()]

    
    print("------------------------------------------------------------")
    print("Part 1")
    part_1(input_lines)

    print("------------------------------------------------------------")
    print("Part 2")
    part_2(input_lines)
