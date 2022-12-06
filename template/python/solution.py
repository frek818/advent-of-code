from aocd.models import Puzzle

DAY = None 
YEAR = None
assert DAY and YEAR, "Day and year must be set"

def solution_1(input_data):
    return 1

def solution_2(input_data):
    return 1

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
    
