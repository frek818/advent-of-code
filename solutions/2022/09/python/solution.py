"""
--- Day 9: Rope Bridge ---
"""
from functools import reduce
from typing import List, Tuple
from aocd.models import Puzzle


class Knot:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, direction):
        match direction:
            case "L":
                self._x -= 1
            case "U":
                self._y += 1
            case "R":
                self._x += 1
            case "D":
                self._y -= 1

    def position(self):
        return (self._x, self._y)


def parse_moves(input_data: str):
    return (
        (direction, int(steps))
        for direction, steps in [
            line.split(" ") for line in input_data.splitlines() if line
        ]
    )


def move_head(knot: Knot, move: str) -> Knot:
    knot.move(move)
    return knot


def move_tail(knot_h: Knot, knot_t: Knot) -> Knot:
    bx, by = knot_t.position()
    ax, ay = knot_h.position()
    if not (abs(ay - by) == 2 or abs(ax - bx) == 2):
        return knot_t
    if ax != bx and ay != by:
        knot_t.move("U") if ay > by else knot_t.move("D")
        knot_t.move("R") if ax > bx else knot_t.move("L")
    elif ax == bx:
        knot_t.move("U") if ay > by else knot_t.move("D")
    elif ay == by:
        knot_t.move("R") if ax > bx else knot_t.move("L")
    return knot_t


def tail_visited_count(knots: List[Knot], moves: Tuple[str, int]) -> int:
    return len(
        set(
            reduce(move_tail, knots[1:], move_head(knots[0], direction)).position()
            for direction, steps in moves
            for _ in range(steps)
        )
    )


def solution_1(input_data: str):
    "part 1"
    return tail_visited_count([Knot(0, 0) for _ in range(2)], parse_moves(input_data))


def solution_2(input_data: str):
    "part 2"
    return tail_visited_count([Knot(0, 0) for _ in range(10)], parse_moves(input_data))


year, day = 2022, 9
assert year and day, "year and day must be set"

if __name__ == "__main__":
    puzzle = Puzzle(year=year, day=day)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
