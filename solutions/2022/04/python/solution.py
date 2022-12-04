from aocd.models import Puzzle

DAY = 4
YEAR = 2022


class Range():
    def __init__(self, range):
        self.lower = int(range.split('-')[0])
        self.upper = int(range.split('-')[1])

    def consumes(self, other: "Range"):
        return self.lower <= other.lower and other.upper <= self.upper

    def overlaps(self, other: "Range"):
        return self.lower <= other.lower <= self.upper


def solution_1(input_data):
    count = 0
    for line in input_data.split('\n'):
        pair = line.split(',')
        range1, range2 = Range(pair[0]), Range(pair[1])
        if range1.consumes(range2) or range2.consumes(range1):
            count += 1
    return count


def solution_2(input_data):
    count = 0
    for line in input_data.split('\n'):
        pair = line.split(',')
        range1, range2 = Range(pair[0]), Range(pair[1])
        if range1.overlaps(range2) or range2.overlaps(range1):
            count += 1
    return count


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
