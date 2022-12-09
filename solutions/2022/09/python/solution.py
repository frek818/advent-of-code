"""
--- Day 9: Rope Bridge ---
"""
from typing import List
from aocd.models import Puzzle


class Knot:
    def __init__(self, x, y, id: int):
        self._x = x
        self._y = y
        self._id = id

    @property
    def id(self) -> str:
        if self._id == 0:
            return "H"
        return str(self._id)

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


def parse_command(line: str):
    direction, steps = line.split(" ")
    return direction, int(steps)


def control_a(thing: Knot, direction):
    thing.move(direction)
    return thing.position()


def control_b(thing: Knot, following_position):
    bx, by = thing.position()
    ax, ay = following_position

    # diagonal procedure
    if ax != bx and ay != by:
        if not (abs(ay - by) == 2 or abs(ax - bx) == 2):
            return

        if ax > bx:
            thing.move("R")
        else:
            thing.move("L")

        if ay > by:
            thing.move("U")
        else:
            thing.move("D")

    # horizontal procedure
    elif ax == bx:
        if abs(ay - by) == 2:
            if ay > by:
                thing.move("U")
            else:
                thing.move("D")

    # vertical procedure
    elif ay == by:
        if abs(ax - bx) == 2:
            if ax > bx:
                thing.move("R")
            else:
                thing.move("L")

    return thing.position()


def tick(things: List[Knot], first_move):
    control_a(things[0], first_move)
    for tail_index in range(1, len(things)):
        control_b(things[tail_index], things[tail_index - 1].position())


def get_grid_boundaries(positions):
    xs = [a[0] for a in positions]
    ys = [a[1] for a in positions]
    left_bound = min(xs)
    right_bound = max(xs)
    lower_bound = min(ys)
    upper_bound = max(ys)
    vertical_range = range(upper_bound, lower_bound - 1, -1)
    horizontal_range = range(left_bound, right_bound + 1)
    return vertical_range, horizontal_range


def print_positions(things: List[Knot], visited_locations: List[Knot]):
    vertical_range, horizontal_range = get_grid_boundaries(visited_locations)
    position_to_thing_map = {thing.position(): thing for thing in things}
    for y in vertical_range:
        for x in horizontal_range:
            thing = position_to_thing_map.get((x, y))
            print("." if thing is None else thing.id, end="")
        print()
    print()


def tail_visited_locations(things, moves, print_board=False):
    visited_locations = []
    for direction, steps in moves:
        for _ in range(steps):
            tick(things, direction)
            visited_locations.append(things[-1].position())
        if print_board:
            print_positions(things, visited_locations)
    return visited_locations


def solution_1(input_data: str):
    "part 1"
    things = [Knot(0, 0, id) for id in range(2)]
    moves = [parse_command(line) for line in input_data.splitlines() if line]
    visited = tail_visited_locations(things, moves)
    return len(set(visited))


def solution_2(input_data: str):
    "part 2"
    things = [Knot(0, 0, id) for id in range(10)]
    moves = [parse_command(line) for line in input_data.splitlines() if line]
    visited = tail_visited_locations(things, moves)
    return len(set(visited))


year, day = 2022, 9
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
