'''Day 1: Calorie Counting'''
from aocd.models import Puzzle

YEAR = 2022
DAY = 1

def parse_elves_calories(input_data):
    'parse elves calories'
    return [[int(cal) for cal in group.split('\n') if cal]
        for group in input_data.split("\n\n")
    ]

def solution_1(input_data):
    '''Max calories of elves'''
    elves = parse_elves_calories(input_data)
    return max([sum(e_cals) for e_cals in elves])

def solution_2(input_data):
    '''Max calories carried by top n elves'''
    elves = parse_elves_calories(input_data)
    top_n = 3
    calories_sorted_desc = sorted([sum(e_cals) for e_cals in elves], reverse=True)
    return sum(calories_sorted_desc[0:top_n])

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
    
