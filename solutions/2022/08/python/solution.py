"""
--- Day 8: Treetop Tree House ---
"""
from aocd.models import Puzzle


def parse_trees(input_data):
    return [[int(t) for t in line] for line in input_data.splitlines()]


def get_tallest_index(items):
    tallest_idx = 0
    tallest = items[0]
    for idx, height in enumerate(items):
        if height > tallest:
            tallest = height
            tallest_idx = idx
    return tallest_idx


def filter_incrementing_indexes(items):
    incrementing = [0]
    previous = items[0]
    for i in range(1, len(items)):
        if items[i] > previous:
            incrementing.append(i)
            previous = items[i]
    return incrementing


def actual_index(indexes, length, direction):
    if direction in ("right", "bottom"):
        return [
            compliment for current, compliment in zip(
                range(length), range(
                    length - 1, -1, -1)) if current in indexes]
    return indexes


def items_visible_from_direction(trees, direction):
    if direction in ("left", "right"):
        outer_dimension = trees
        inner_dimension = trees[0]
    else:
        outer_dimension = trees[0]
        inner_dimension = trees

    visible = []
    for outer in range(len(outer_dimension)):
        all_in_row = actual_direction(
            [
                tree_height(
                    inner,
                    outer,
                    direction,
                    trees) for inner in range(
                    len(inner_dimension))],
            direction)
        tallest_index = get_tallest_index(all_in_row)
        incrementing_indexes = actual_index(filter_incrementing_indexes(
            all_in_row[:tallest_index + 1]), len(inner_dimension), direction)
        for idx in incrementing_indexes:
            visible.append(actual_coords(idx, outer, direction))
    return visible


def actual_direction(items, direction):
    if direction in ("right", "bottom"):
        return list(reversed(items))
    return items


def actual_coords(index, outer, direction):
    if direction in ("left", "right"):
        return (index, outer)
    return (outer, index)


def tree_height(inner, outer, direction, trees):
    if direction in ("left", "right"):
        return trees[outer][inner]
    return trees[inner][outer]


def scenic_score(x, y, trees):
    if x == 0 or y == 0 or x + 1 == len(trees[0]) or y + 1 == len(trees):
        return 0
    left = viewing_distance(x, y, trees, "left")
    top = viewing_distance(x, y, trees, "top")
    right = viewing_distance(x, y, trees, "right")
    bottom = viewing_distance(x, y, trees, "bottom")
    return left * top * right * bottom


def viewing_distance(x, y, trees, direction):
    if direction == "left":
        neighbors = [(v, y) for v in range(x - 1, -1, -1)]
    elif direction == "top":
        neighbors = [(x, v) for v in range(y - 1, -1, -1)]
    elif direction == "right":
        neighbors = [(v, y) for v in range(x + 1, len(trees[0]))]
    elif direction == "bottom":
        neighbors = [(x, v) for v in range(y + 1, len(trees))]

    viewable_trees = 0
    height = trees[y][x]
    for nx, ny in neighbors:
        viewable_trees += 1
        if trees[ny][nx] >= height:
            break
        if nx == 0 or ny == 0 or nx + \
                1 == len(trees[0]) or ny + 1 == len(trees):
            break
    return viewable_trees


def solution_1(input_data: str):
    "part 1"
    trees = parse_trees(input_data)
    visible = set()
    for direction in ("left", "top", "right", "bottom"):
        for item in items_visible_from_direction(trees, direction):
            visible.add(item)
    return len(visible)


def solution_2(input_data: str):
    "part 2"
    trees = parse_trees(input_data)
    highest_score = -1
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            score = scenic_score(x, y, trees)
            if score > highest_score:
                highest_score = score
    return highest_score


year, day = 2022, 8
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
