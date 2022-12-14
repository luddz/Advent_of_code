import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

def part_1(input_lines):
    eval_at = [20, 60, 100, 140, 180, 220]
    cycles_passed = 0
    signal_strenght = 0
    register = 1
    for instruction in  input_lines:
        if instruction == "noop":
            if cycles_passed + 1 in eval_at:
                a = (cycles_passed + 1) * register
                signal_strenght += a
                print(f"{cycles_passed + 1} - {register} = {a}")
            cycles_passed += 1
        else:
            if cycles_passed + 1 in eval_at:
                a = (cycles_passed + 1) * register
                signal_strenght += a
                print(f"{cycles_passed + 1} - {register} = {a}")
            
            if cycles_passed + 2 in eval_at:
                a = (cycles_passed + 2) * register
                signal_strenght += a
                print(f"{cycles_passed + 2} - {register} = {a}")

            cycles_passed += 2
            register += int(instruction.split(" ")[1])

    print(f"{signal_strenght = }")


def print_sprite(sprite):
    chunk_size = len(sprite)//6
    res = [sprite[i:i+chunk_size] for i in range(0, len(sprite), chunk_size) ]
    for l in res:
        for c in l:
            print(c, end="")
        print()


def get_sprite_span(draw_p, reg):
    r_len = 40
    for i in range(0,6):
        if i * r_len <= draw_p < (i + 1) * r_len:
            base = i * r_len 
            return [base + (reg-1), base + reg, base + (reg + 1)]


def draw(draw_p, reg):
    return "#" if draw_p in get_sprite_span(draw_p, reg) else "."


def part_2(input_lines):
    sprite_as_line = ["." for _ in range(240)]
    draw_pos = 0
    register = 1
    for instruction in  input_lines:
        if instruction == "noop":
            sprite_as_line[draw_pos] = draw(draw_pos, register)
            draw_pos += 1
        else:
            for _ in range(2):
                sprite_as_line[draw_pos] = draw(draw_pos, register)
                draw_pos += 1

            register += int(instruction.split(" ")[1])
    print_sprite(sprite_as_line)
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
