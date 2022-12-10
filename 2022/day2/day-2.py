example_input = "example.txt"
test_input = "test.txt"

input_lines = []
file = test_input
with open(file, 'r') as f:
    input_lines = f.readlines()

total_score = 0
win_score = 6
draw_score = 3
rock_score = 1
papper_score = 2
scissor_score = 3

scores = [papper_score, rock_score, scissor_score] 
def part_2():
    total_score = 0
    look_up = {
        "B": papper_score,
        "A": rock_score, 
        "C": scissor_score,
        "X" : 0, #Lose score
        "Y": draw_score,
        "Z": win_score
    }

    def get_loosing_play(oponent):
        if oponent == papper_score:
            return rock_score
        elif oponent == rock_score:
            return scissor_score
        elif oponent == scissor_score:
            return papper_score
    
    def get_winnig_play(oponent):
        if oponent == papper_score:
            return scissor_score
        elif oponent == rock_score:
            return papper_score
        elif oponent == scissor_score:
            return rock_score

    for line in input_lines:
        plays = line.strip().split(" ")
        oponent, end_result = look_up[plays[0]], look_up[plays[1]] 
        total_score += end_result
        if end_result == 0:
            total_score += get_loosing_play(oponent)
        elif end_result == draw_score:
            total_score += oponent
        elif end_result == win_score:
            total_score += get_winnig_play(oponent)

    print (f"{total_score = }")



def part_1():
    total_score = 0
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
