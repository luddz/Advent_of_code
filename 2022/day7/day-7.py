import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

@dataclass
class File:
    size: int
    name: str

@dataclass
class Director:
    name: str
    files: dict
    size: int
    parent: object

file_system = Director("/",{}, 0, Director)
tmp = None

def handle_cmd(line):
    global tmp 
    global file_system
    cmd = line.split(" ")
    if cmd[1] == "cd":
        if cmd[2] == "..":
            if tmp.parent != None: # We are not at the root
                tmp = tmp.parent
        elif  cmd[2] == "/":
            a = tmp if tmp != None else file_system
            while(a.name != "/"):
                a = a.parent
            tmp = a
        else:
            for f, v in tmp.files.items():
                if f == cmd[2]:
                    tmp = v


total_dir_size = 0
def get_dir_file_size(dir):
    global total_dir_size
    total_size = 0 
    for _, v in dir.files.items():
        if type(v) is File:
            total_size += v.size
        if type(v) is Director:
            total_size += get_dir_file_size(v)

    dir.size = total_size
    if dir.size <= 100000:
        total_dir_size += dir.size
    return total_size


def part_1(input_lines):
    global tmp 
    global file_system
    for line in input_lines:
        if line[0] == "$":
            handle_cmd(line)
        else:
            # Result of a ls command
            l = line.split(" ")
            if l[0] == "dir": # Found a dir, adding it
                if l[1] not in tmp.files:
                    d = Director(l[1], {}, 0, tmp)
                    tmp.files[l[1]] = d
            else: # create file
                if l[1] not in tmp.files:
                    f = File(int(l[0]), l[1])
                    tmp.files[l[1]] = f
    
    print("------------------------------------------------------------")
    a = tmp
    while(a.name != "/"):
        a = a.parent
    get_dir_file_size(a)
    print(f"{total_dir_size = }")
    part_2(a)
    return

tot_space = 70000000
smalest_dir_to_del = Director("", {}, tot_space, None)
def find_smallest_to_remove(dir, to_del):
    global smalest_dir_to_del
    for _, v in dir.files.items():
        if type(v) is Director:
            if v.size >= to_del and v.size < smalest_dir_to_del.size and v.name != smalest_dir_to_del.name:
                smalest_dir_to_del = v
            find_smallest_to_remove(v, to_del)

def part_2(fs):
    print("------------------------------------------------------------")
    print("Part 2")
    needed_space = 30000000
    to_del = needed_space - (tot_space - fs.size)
    find_smallest_to_remove(fs, to_del)
    print(f"{smalest_dir_to_del.name } -- {smalest_dir_to_del.size}")
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
    # part_2(input_lines)
