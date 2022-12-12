"""
--- Day 12: Hill Climbing Algorithm ---
"""
import os

from aocd.models import Puzzle


def solution_1(input_data: str):
    "part 1"
    return 0


def solution_2(input_data: str):
    "part 2"
    return 0


year, day = 2022, 12
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    for _ in range(int(os.getenv("TIMES","1"))):
        print(solution_1(puzzle.input_data))
        print(solution_2(puzzle.input_data))