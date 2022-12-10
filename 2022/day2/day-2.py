from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"

class Scores(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSOR = 3

@dataclass
class Node:
    iam: Scores
    wins: Scores
    loses: Scores

input_lines = []
file = test_input
with open(file, 'r') as f:
    input_lines = f.readlines()

total_score = 0
win_score = 6
draw_score = 3

def part_2():
    total_score = 0
    look_up = {
        "B": Node(Scores.PAPPER, Scores.ROCK, Scores.SCISSOR),
        "A": Node(Scores.ROCK, Scores.SCISSOR, Scores.PAPPER), 
        "C": Node(Scores.SCISSOR, Scores.PAPPER, Scores.ROCK),
        "X" : 0, #Lose score
        "Y": draw_score,
        "Z": win_score
    }
    
    for line in input_lines:
        plays = line.strip().split(" ")
        oponent, end_result = look_up[plays[0]], look_up[plays[1]] 
        total_score += end_result
        if end_result == 0:
            total_score += oponent.wins.value
        elif end_result == draw_score:
            total_score += oponent.iam.value
        elif end_result == win_score:
            total_score += oponent.loses.value

    print (f"{total_score = }")



def part_1():
    total_score = 0
    rock_score = 1
    papper_score = 2
    scissor_score = 3
    look_up = {
        "B": papper_score,
        "Y": papper_score,
        "A": rock_score, 
        "X" : rock_score,
        "C": scissor_score,
        "Z": scissor_score
    }
    def check_result(oponent, you):
        if you == oponent:
            return draw_score
        elif (you == rock_score and oponent == scissor_score) or \
            you == papper_score and oponent == rock_score or \
            you == scissor_score and oponent == papper_score:
            return win_score
        return 0

    for line in input_lines:
        plays = line.strip().split(" ")
        oponent, you  = look_up[plays[0]], look_up[plays[1]]
        total_score += you + check_result(oponent, you)

    print (f"{total_score = }")

print("------------------------------------------------------------")
print("Part 1")
part_1()

print("------------------------------------------------------------")
print("Part 2")
part_2()
