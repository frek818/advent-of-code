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
        
        if len(elf):
            elves.append(elf)
            elf = []
    return elves

def solution_1(input_data):
    '''Max calories of elves'''
    elves = parse_elves_calories(input_data)
    return max(sum(e_cals) for e_cals in elves)
    
if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    print(solution_1(puzzle.input_data))
