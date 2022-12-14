import argparse
from enum import Enum
from dataclasses import dataclass

example_input = "example.txt"
test_input = "test.txt"


def look(tree_map, hidden_map):
    # This could be done from all four sides at the same time.
    # and with numpy for performance 
    for i, line in enumerate(tree_map):
        highest_tree_from_left = -1
        highest_tree_from_right = -1 
        for j in range(len(line)):
            if highest_tree_from_left == 9 and highest_tree_from_right == 9:
                break
            
            tree_on_left = tree_map[i][j]
            tree_on_right = tree_map[i][-(j+1)]
            if tree_on_left > highest_tree_from_left :
                hidden_map[i][j] = 0
                highest_tree_from_left = tree_on_left
            
            if tree_on_right > highest_tree_from_right: ## Here is le error
                hidden_map[i][-(j+1)] = 0
                highest_tree_from_right = tree_on_right
    return hidden_map

def transponse_matrix(l1):
    return [[r[i] for r in l1] for i in range(len(l1[0]))]

def part_1(input_lines):
    tree_height_map = []
    hidden_map = []
    for line in input_lines:
        tree_height_map.append([int(l) for l in line])
        hidden_map.append([1 for _ in line])
    h_map = look(tree_height_map, hidden_map)
    inv_tree = transponse_matrix(tree_height_map)
    inv_hidden = transponse_matrix(h_map)
    res = look(inv_tree, inv_hidden)
    for l in transponse_matrix(res): 
        print(l)
    h = 0
    for a in res:
        for b in a:
            if b == 0:
                h += 1

    print(f"Visible trees {h}")
    return

def part_2(input_lines):
    tree_height_map = []
    scenic_score = []
    for line in input_lines:
        tree_height_map.append([int(l) for l in line])
        scenic_score.append([1 for _ in line])

    sc = find_scenic_score(tree_height_map, scenic_score)
    return


def find_scenic_score(tree_map, scenic_score):
    
    mat_h = len(tree_map)
    max = 0
    for i, line in enumerate(tree_map):
        for j, tree_h in enumerate(line):
            shorter_trees_top = 0 
            shorter_trees_bottom = 0
            shorter_trees_left = 0
            shorter_trees_right = 0
            
            for a in range(i-1, -1, -1):
                shorter_trees_top += 1
                if tree_map[a][j] >= tree_h:
                    break

            for a in range(i+1, mat_h):
                shorter_trees_bottom += 1
                if tree_map[a][j] >= tree_h:
                    break

            for a in range(j-1, -1, -1):
                shorter_trees_left += 1
                if tree_map[i][a] >= tree_h:
                    break
                
            for a in range(j+1, len(line)):
                shorter_trees_right += 1
                if tree_map[i][a] >= tree_h:
                    break
            
            sc =  shorter_trees_left * shorter_trees_top * shorter_trees_right * shorter_trees_bottom
            if sc > max: 
                max = sc
    
    print(f"Max Scenic score: {max}")

    return scenic_score



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
