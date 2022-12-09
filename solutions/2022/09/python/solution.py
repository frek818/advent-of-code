"""
--- Day 9: Rope Bridge ---
"""
from typing import List
from aocd.models import Puzzle


class Thing:
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


def parse_command(direction: str, step: str):
    return direction, int(step)


def control_a(thing: Thing, direction):
    thing.move(direction)
    return thing.position()


def control_b(thing: Thing, following_position):
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


def tick(thing_a, thing_b, a_command):
    a_position = control_a(thing_a, a_command)
    control_b(thing_b, a_position)


def tick_many(things: List[Thing], first_move):
    control_a(things[0], first_move)
    control_b(things[1], things[0].position())
    control_b(things[2], things[1].position())
    control_b(things[3], things[2].position())
    control_b(things[4], things[3].position())
    control_b(things[5], things[4].position())
    control_b(things[6], things[5].position())
    control_b(things[7], things[6].position())
    control_b(things[8], things[7].position())
    control_b(things[9], things[8].position())


def solution_1(input_data: str):
    "part 1"
    thing_a = Thing(0, 0, "1")
    thing_b = Thing(0, 0, "2")
    unique_locations = []

    for line in input_data.split("\n"):
        if not line:
            continue
        direction, steps = parse_command(*line.split(" "))
        for _ in range(steps):
            tick(thing_a, thing_b, direction)
            unique_locations.append(thing_b.position())
    return len(set(unique_locations))


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


def print_positions(things: List[Thing]):
    positions = [thing.position() for thing in things]
    vertical_range, horizontal_range = get_grid_boundaries(positions)
    position_to_thing_map = {thing.position(): thing for thing in things}
    for y in vertical_range:
        for x in horizontal_range:
            thing = position_to_thing_map.get((x, y))
            print("." if thing is None else thing.id, end="")
        print()


def solution_2(input_data: str):
    "part 2"
    things = [Thing(0, 0, id) for id in range(10)]
    locations = []
    for line in input_data.split("\n"):
        if not line:
            continue
        direction, steps = parse_command(*line.split(" "))
        for _ in range(steps):
            tick_many(things, direction)
            locations.append(things[9].position())
        print_positions(things)
    return len(set(locations))


year, day = 2022, 9
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
