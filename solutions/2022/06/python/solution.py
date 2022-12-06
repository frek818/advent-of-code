from aocd.models import Puzzle


def marker_finder(input_data, distinct):
    answer = None
    for start_idx in range(len(input_data) - distinct + 1):
        uniq_characters = len(set(input_data[start_idx:start_idx + distinct]))
        if uniq_characters == distinct:
            answer = start_idx + distinct
            break
    return answer


def solution_1(input_data):
    return marker_finder(input_data, 4)


def solution_2(input_data):
    return marker_finder(input_data, 14)


year, day = None, None
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=DAY)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
