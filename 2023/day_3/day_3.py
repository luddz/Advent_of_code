import argparse

example_input = "example.txt"
test_input = "test.txt"


def generate_matrix(input_lines: list) -> list[list]:
    return [[c for c in row] for row in input_lines]


def part_1(input_lines):
    numbers = [str(i) for i in range(10)]
    matrix = generate_matrix(input_lines=input_lines)

    def check_engine_symbol(row: int, column: int) -> bool:
        if 0 <= row < len(matrix) and 0 <= column < len(matrix[0]):
            char = matrix[row][column]
            return char not in numbers and char != "."
        return False

    sum_ = []
    for r in range(len(matrix)):
        current_num = ""
        symbol_around = False
        for c in range(len(matrix[r])):
            symbol = matrix[r][c]

            if symbol in numbers:
                current_num += symbol
                if len(current_num) == 1:
                    # Check to the left, above left, below left.
                    if check_engine_symbol(r - 1, c - 1) or check_engine_symbol(r, c - 1) or check_engine_symbol(r + 1, c - 1):
                        symbol_around = True
                # Check above and below
                if check_engine_symbol(r - 1, c) or check_engine_symbol(r + 1, c):
                    symbol_around = True

                if c != len(matrix[r])-1:
                    continue

            if current_num != "":
                t = check_engine_symbol(r - 1, c) or check_engine_symbol(r, c) or check_engine_symbol(r + 1, c)
                if (symbol_around or t):
                    sum_.append(int(current_num))

            current_num = ""
            symbol_around = False

    print(sum_)
    print(f"Result part1: {sum(sum_)}")
    return


def part_2(input_lines):
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-e","--example", action='store_true')
    args = parser.parse_args()

    input_lines = []
    file = test_input if not args.example else example_input
    p = r"/Users/ludvigkindberg/git-repos/Advent_of_code/2023/day_3/"
    with open(p+file, 'r') as f:
        input_lines = [l.strip() for l in f.readlines()]

    print("------------------------------------------------------------")
    print("Part 1")
    part_1(input_lines)

    print("------------------------------------------------------------")
    print("Part 2")
    part_2(input_lines)
