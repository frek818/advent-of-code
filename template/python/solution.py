from aocd.models import Puzzle


def solution_1(input_data):
    'part 1'
    return 1


def solution_2(input_data):
    'part 2'
    return 1


year, day = None, None
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
