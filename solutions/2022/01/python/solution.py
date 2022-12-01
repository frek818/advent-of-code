'''Day 1: Calorie Counting'''
from aocd.models import Puzzle

def parse_elves_calories(input_data):
    'parse elves calories'
    lines = [l.strip() for l in input_data.split("\n")]

    elves = []
    elf = []
    for line in lines:
        if line.strip() != '':
            elf.append(int(line))
            continue
        if len(elf) == 0:
            elves.append(elf)
            elf = []
    if len(elf) != 0:
        elves.append(elf)
    return elves

def solution_1(input_data):
    '''Max calories of elves'''
    elves = parse_elves_calories(input_data)
    return max(sum(e_cals) for e_cals in elves)

def solution_2(input_data):
    '''Max calories carried by top n elves'''
    elves = parse_elves_calories(input_data)
    top_n = 3
    calories_sorted_desc = sorted([sum(e_cals) for e_cals in elves], reverse=True)
    return sum(calories_sorted_desc[0:top_n])

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
    
